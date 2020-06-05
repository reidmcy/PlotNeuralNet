import sys
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    #input
    to_input( 'chess.png' ),
    *conv_block(name='conv_block1', s_filer=8, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=35, depth=35, opacity=0.5),
    # to_ConvBatchNorm( name='conv_block1', s_filer=8, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40),
    # to_Relu(name="conv_block1_relu", offset="(0,0,0)", to="(conv_block1-east)", width=0.5, height=40, depth=40, opacity=0.5),    
    *block_Res_2( name='res_0', botton='conv_block1_relu', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *block_Res_2( name='res_1', botton='res_0_skip', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *block_Res_2( name='res_2', botton='res_1_skip', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *block_Res_2( name='res_3', botton='res_2_skip', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *block_Res_2( name='res_4', botton='res_3_skip', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *block_Res_2( name='res_5', botton='res_4_skip', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *policy_head( name='policy_head', botton='res_5_add_relu', s_filer=8, n_filer=64, offset="(4.5,4.5,0)", width=2, height=35, depth=35, opacity=0.5),
    *invisible_box( name='invisible', botton='res_5_add_relu', offset="(2,-4.5,0)", width=0, height=0, depth=0, opacity=0),
    *value_head( name='value_head', botton='invisible', s_filer=8, n_filer=32, offset="(2.5,0,0)", width=1.5, height=35, depth=35, opacity=0.5),

    to_end()
    ]


def main():
    to_generate(arch, 'network_diagram_maia.tex' )

if __name__ == '__main__':
    main()
