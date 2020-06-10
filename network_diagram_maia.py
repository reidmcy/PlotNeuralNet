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
    *invisible_box_2( name='invisible_1', botton='conv_block1_relu', offset="(1.5,0,0)", width=1, height=13, depth=13, opacity=0, caption='\makebox[12pt]{\shortstack[c]{Gradient Stop \\\ Location}}'),
    *invisible_box_2_no_connection( name='invisible_1_cap', botton='invisible_1', offset="(-0.5,-3.1,0)", width=0, height=0, depth=0, opacity=0, caption='\makebox[0pt]{\shortstack[c]{9}}'),
    
    # to_ConvBatchNorm( name='conv_block1', s_filer=8, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40),
    # to_Relu(name="conv_block1_relu", offset="(0,0,0)", to="(conv_block1-east)", width=0.5, height=40, depth=40, opacity=0.5),    
    *block_Res_2( name='res_0', botton='invisible_1', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *invisible_box_2( name='invisible_2', botton='res_0_add_relu', offset="(1.5,0,0)", width=1, height=13, depth=13, opacity=0, caption='\makebox[12pt]{\shortstack[c]{Gradient Stop \\\ Location}}'),
    *invisible_box_2_no_connection( name='invisible_2_cap', botton='invisible_2', offset="(-0.5,-3.1,0)", width=0, height=0, depth=0, opacity=0, caption='\makebox[0pt]{\shortstack[c]{8}}'),

    
    *block_Res_2( name='res_1', botton='invisible_2', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *invisible_box_2( name='invisible_3', botton='res_1_add_relu', offset="(1.5,0,0)", width=1, height=13, depth=13, opacity=0, caption='\makebox[12pt]{\shortstack[c]{Gradient Stop \\\ Location}}'),
    *invisible_box_2_no_connection( name='invisible_3_cap', botton='invisible_3', offset="(-0.5,-3.1,0)", width=0, height=0, depth=0, opacity=0, caption='\makebox[0pt]{\shortstack[c]{7}}'),
    
    *block_Res_2( name='res_2', botton='invisible_3', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *invisible_box_2( name='invisible_4', botton='res_2_add_relu', offset="(1.5,0,0)", width=1, height=13, depth=13, opacity=0, caption='\makebox[12pt]{\shortstack[c]{Gradient Stop \\\ Location}}'),
    *invisible_box_2_no_connection( name='invisible_4_cap', botton='invisible_4', offset="(-0.5,-3.1,0)", width=0, height=0, depth=0, opacity=0, caption='\makebox[0pt]{\shortstack[c]{6}}'),
    
    *block_Res_2( name='res_3', botton='invisible_4', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *invisible_box_2( name='invisible_5', botton='res_3_add_relu', offset="(1.5,0,0)", width=1, height=13, depth=13, opacity=0, caption='\makebox[12pt]{\shortstack[c]{Gradient Stop \\\ Location}}'),
    *invisible_box_2_no_connection( name='invisible_5_cap', botton='invisible_5', offset="(-0.5,-3.1,0)", width=0, height=0, depth=0, opacity=0, caption='\makebox[0pt]{\shortstack[c]{5}}'),
    
    *block_Res_2( name='res_4', botton='invisible_5', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *invisible_box_2( name='invisible_6', botton='res_4_add_relu', offset="(1.5,0,0)", width=1, height=13, depth=13, opacity=0, caption='\makebox[12pt]{\shortstack[c]{Gradient Stop \\\ Location}}'),
    *invisible_box_2_no_connection( name='invisible_6_cap', botton='invisible_6', offset="(-0.5,-3.1,0)", width=0, height=0, depth=0, opacity=0, caption='\makebox[0pt]{\shortstack[c]{4}}'),
    
    *block_Res_2( name='res_5', botton='invisible_6', s_filer=8, n_filer=64, offset="(2,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *invisible_box_3( name='invisible_7', botton='res_5_add_relu', offset="(1.5,4.5,0)", width=1, height=13, depth=13, opacity=0, caption='\makebox[12pt]{\shortstack[c]{Gradient Stop \\\ Location}}'),
    *invisible_box_2_no_connection( name='invisible_7_cap', botton='invisible_7', offset="(-0.5,-3.1,0)", width=0, height=0, depth=0, opacity=0, caption='\makebox[0pt]{\shortstack[c]{3}}'),

    # *policy_head( name='policy_head', botton='res_5_add_relu', s_filer=8, n_filer=64, offset="(4.5,4.5,0)", width=2, height=35, depth=35, opacity=0.5),

    *policy_head( name='policy_head', botton='invisible_7', s_filer=8, n_filer=64, offset="(2.3,0,0)", width=2, height=35, depth=35, opacity=0.5),
    *invisible_box( name='invisible', botton='res_5_add_relu', offset="(1.8,-4.5,0)", width=0, height=0, depth=0, opacity=0),
    *value_head( name='value_head', botton='invisible', s_filer=8, n_filer=32, offset="(2.2,0,0)", width=1.5, height=35, depth=35, opacity=0.5),

    to_end()
    ]


def main():
    to_generate(arch, 'network_diagram_maia.tex' )

if __name__ == '__main__':
    main()
