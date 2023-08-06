from functools import partial

from torch import nn
import torch
from torch.nn.modules.transformer import _get_activation_fn, Module, Tensor, Optional, MultiheadAttention, Linear, Dropout, LayerNorm
from torch.utils.checkpoint import checkpoint
from einops import rearrange

# added by Ugne (before it showed error: F is not defined)
from torch.nn import functional as F


class TransformerEncoderLayer(Module):
    r"""TransformerEncoderLayer is made up of self-attn and feedforward network.
    This standard encoder layer is based on the paper "Attention Is All You Need".
    Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
    Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In Advances in
    Neural Information Processing Systems, pages 6000-6010. Users may modify or implement
    in a different way during application.

    Args:
        d_model: the number of expected features in the input (required).
        nhead: the number of heads in the multiheadattention models (required).
        dim_feedforward: the dimension of the feedforward network model (default=2048).
        dropout: the dropout value (default=0.1).
        activation: the activation function of intermediate layer, relu or gelu (default=relu).
        layer_norm_eps: the eps value in layer normalization components (default=1e-5).
        batch_first: If ``True``, then the input and output tensors are provided
            as (batch, seq, feature). Default: ``False``.

    Examples::
        >>> encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8)
        >>> src = torch.rand(10, 32, 512)
        >>> out = encoder_layer(src)

    Alternatively, when ``batch_first`` is ``True``:
        >>> encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8, batch_first=True)
        >>> src = torch.rand(32, 10, 512)
        >>> out = encoder_layer(src)
    """
    __constants__ = ['batch_first']
    # src - batched input
    def __init__(self, d_model, emsize_f, nhead, dim_feedforward=2048, dropout=0.1, activation="relu",
                 layer_norm_eps=1e-5, batch_first=False, pre_norm=False,
                 device=None, dtype=None, recompute_attn=False) -> None:
        factory_kwargs = {'device': device, 'dtype': dtype}
        super().__init__()
        self.self_attn = MultiheadAttention(d_model, nhead, dropout=dropout, batch_first=batch_first,
                                            **factory_kwargs)
        
        # Implementation of Feedforward model
        
        # self.pre_linear2 = Linear(1, d_model, **factory_kwargs)
        # self.pre_linear4 = Linear(d_model, 1, **factory_kwargs)
        # self.inter_feature_attn_2 = MultiheadAttention(d_model, nhead, dropout=dropout, batch_first=batch_first,
        #                                     **factory_kwargs)
        # self.pre_norm2 = LayerNorm(d_model, eps=layer_norm_eps, **factory_kwargs)
        
        ############################## Inter-feature attention ############################################
        self.pre_linear1 = Linear(1, emsize_f, **factory_kwargs)
        
        self.inter_feature_attn = MultiheadAttention(emsize_f, 4, dropout=dropout, batch_first=batch_first,
                                            **factory_kwargs)
        
        self.pre_linear2 = Linear(emsize_f, dim_feedforward, **factory_kwargs)
        self.pre_linear3 = Linear(dim_feedforward, 1, **factory_kwargs)
        
        self.pre_norm_ = LayerNorm(emsize_f, eps=layer_norm_eps, **factory_kwargs)
        self.pre_dropout = Dropout(dropout)
        
        self.pre_linear4 = Linear(emsize_f, dim_feedforward, **factory_kwargs)
        self.pre_linear5 = Linear(dim_feedforward, d_model, **factory_kwargs)
        ####################################################################################################
        
        self.linear1 = Linear(d_model, dim_feedforward, **factory_kwargs)
        self.dropout = Dropout(dropout)
        self.linear2 = Linear(dim_feedforward, emsize_f, **factory_kwargs)

        self.norm1 = LayerNorm(d_model, eps=layer_norm_eps, **factory_kwargs)
        self.norm2 = LayerNorm(emsize_f, eps=layer_norm_eps, **factory_kwargs)
        self.dropout1 = Dropout(dropout)
        self.dropout2 = Dropout(dropout)
        self.pre_norm = pre_norm
        self.recompute_attn = recompute_attn

        self.activation = _get_activation_fn(activation)

    def __setstate__(self, state): # not sure what it does
        if 'activation' not in state:
            state['activation'] = F.relu
        super().__setstate__(state)

    def forward(self, src: Tensor, src_mask: Optional[Tensor] = None, src_key_padding_mask: Optional[Tensor] = None) -> Tensor:
        r"""Pass the input through the encoder layer.

        Args:
            src: the sequence to the encoder layer (required).
            src_mask: the mask for the src sequence (optional).
            src_key_padding_mask: the mask for the src keys per batch (optional).

        Shape:
            see the docs in Transformer class.
        """
        if self.pre_norm: # NOT RUN: pre_norm=False by default and is not changed in model=TransformerModel() in train.py
            src_ = self.norm1(src)
        else: # this gets RUN
            src_ = src
        if isinstance(src_mask, tuple): # NOT RUN - AssertionError 
            # global attention setup
            assert not self.self_attn.batch_first # AssertionError when batch_first=True: not True = False  --> so batch_first must be False (and it is - default False is not changed in model=TransformerModel() in train.py)
            assert src_key_padding_mask is None # AssertionError when src_key_padding_mask=None --> so src_key_padding_mask must be not None (but it is None - default None is not changed)
            
            # I think this is not run as we get AssertionError: default src_key_padding_mask=None is not changed
            # so we actually do what's in else (elif also gets AssertionError fot the same reason)

            global_src_mask, trainset_src_mask, valset_src_mask = src_mask

            num_global_tokens = global_src_mask.shape[0]
            num_train_tokens = trainset_src_mask.shape[0]

            global_tokens_src = src_[:num_global_tokens]
            train_tokens_src = src_[num_global_tokens:num_global_tokens+num_train_tokens]
            global_and_train_tokens_src = src_[:num_global_tokens+num_train_tokens]
            eval_tokens_src = src_[num_global_tokens+num_train_tokens:]

            attn = partial(checkpoint, self.self_attn) if self.recompute_attn else self.self_attn

            global_tokens_src2 = attn(global_tokens_src, global_and_train_tokens_src, global_and_train_tokens_src, None, True, global_src_mask)[0]
            train_tokens_src2 = attn(train_tokens_src, global_tokens_src, global_tokens_src, None, True, trainset_src_mask)[0]
            eval_tokens_src2 = attn(eval_tokens_src, src_, src_,
                                    None, True, valset_src_mask)[0]

            src2 = torch.cat([global_tokens_src2, train_tokens_src2, eval_tokens_src2], dim=0)

        elif isinstance(src_mask, int): # NOT RUN - AssertionError 
            assert src_key_padding_mask is None # AssertionError when src_key_padding_mask=None --> so src_key_padding_mask must be not None (but it is None - default None is not changed)
            single_eval_position = src_mask
            
            ################### The Inter-feature implementation ###########################
            src1 = rearrange(src_, 'b h w -> w (b h) 1') # <- rearrange for Interfeature attention
            src1 = self.pre_linear1(src1) # <- linear layers
            src1 = self.inter_feature_attn(src1, src1, src1)[0] # <- interfeature attention
    
            src1 = self.pre_linear3(self.activation(self.pre_linear2(src1))) # <- linear layers to squeeze everything back up
            src1 = rearrange(src1, 'w (b h) 1 -> b h w', b = src_.size()[0]) 
            src1 = self.pre_norm_(self.pre_dropout(src1)) + src_ # <- residual layer
            src1_ = self.pre_linear5(self.activation(self.pre_linear4(src1))) # <- Activated linear layer to change dimension
            ###############################################################################

            src_right = self.self_attn(src1_[single_eval_position:], src1_[:single_eval_position], 
                                       src1_[:single_eval_position])[0] # <- Intersample implementation right
            
            src2 = torch.cat([src1_[:single_eval_position], src_right], dim=0)
            
        else: # this gets RUN 
            if self.recompute_attn: # recompute_attn=False by default, and is not changed in model=TransformerModel() in train.py)
                src2 = checkpoint(self.self_attn, src_, src_, src_, src_key_padding_mask, True, src_mask)[0]
            else: # so we actually do this part
                src2 = self.self_attn(src_, src_, src_, attn_mask=src_mask,
                                      key_padding_mask=src_key_padding_mask)[0]
        src_o = self.dropout1(src2) 
        if not self.pre_norm: # this gets RUN: pre_norm=False, not False = True
            src_o = self.norm1(src_o) + src1_

        if self.pre_norm: # NOT RUN: pre_norm=False
            src_ = self.norm2(src_o) + src1_
        else: # this gets RUN
            src_ = src_o
            
        src2 = self.linear2(self.activation(self.linear1(src_)))
        src = src1 + self.dropout2(src2)

        if not self.pre_norm: # this gets RUN: pre_norm=False, not False = True
            src = self.norm2(src)
        return src
