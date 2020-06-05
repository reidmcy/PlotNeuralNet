
from .tikzeng import *

#define new block
def block_2ConvPool( name, botton, top, s_filer=256, n_filer=64, offset="(1,0,0)", size=(32,32,3.5), opacity=0.5 ):
    return [
    to_ConvConvRelu( 
        name="ccr_{}".format( name ),
        s_filer=str(s_filer), 
        n_filer=(n_filer,n_filer), 
        offset=offset, 
        to="({}-east)".format( botton ), 
        width=(size[2],size[2]), 
        height=size[0], 
        depth=size[1],   
        ),    
    to_Pool(         
        name="{}".format( top ), 
        offset="(0,0,0)", 
        to="(ccr_{}-east)".format( name ),  
        width=1,         
        height=size[0] - int(size[0]/4), 
        depth=size[1] - int(size[0]/4), 
        opacity=opacity, ),
    to_connection( 
        "{}".format( botton ), 
        "ccr_{}".format( name )
        )
    ]


def block_Unconv( name, botton, top, s_filer=256, n_filer=64, offset="(1,0,0)", size=(32,32,3.5), opacity=0.5 ):
    return [
        to_UnPool(  name='unpool_{}'.format(name),    offset=offset,    to="({}-east)".format(botton),         width=1,              height=size[0],       depth=size[1], opacity=opacity ),
        to_ConvRes( name='ccr_res_{}'.format(name),   offset="(0,0,0)", to="(unpool_{}-east)".format(name),    s_filer=str(s_filer), n_filer=str(n_filer), width=size[2], height=size[0], depth=size[1], opacity=opacity ),       
        to_Conv(    name='ccr_{}'.format(name),       offset="(0,0,0)", to="(ccr_res_{}-east)".format(name),   s_filer=str(s_filer), n_filer=str(n_filer), width=size[2], height=size[0], depth=size[1] ),
        to_ConvRes( name='ccr_res_c_{}'.format(name), offset="(0,0,0)", to="(ccr_{}-east)".format(name),       s_filer=str(s_filer), n_filer=str(n_filer), width=size[2], height=size[0], depth=size[1], opacity=opacity ),       
        to_Conv(    name='{}'.format(top),            offset="(0,0,0)", to="(ccr_res_c_{}-east)".format(name), s_filer=str(s_filer), n_filer=str(n_filer), width=size[2], height=size[0], depth=size[1] ),
        to_connection( 
            "{}".format( botton ), 
            "unpool_{}".format( name ) 
            )
    ]


def block_Res( num, name, botton, top, s_filer=256, n_filer=64, offset="(0,0,0)", size=(32,32,3.5), opacity=0.5 ):
    lys = []
    layers = [ *[ '{}_{}'.format(name,i) for i in range(num-1) ], top]
    for name in layers:        
        ly = [ to_Conv( 
            name='{}'.format(name),       
            offset=offset, 
            to="({}-east)".format( botton ),   
            s_filer=str(s_filer), 
            n_filer=str(n_filer), 
            width=size[2],
            height=size[0],
            depth=size[1]
            ),
            to_connection( 
                "{}".format( botton  ), 
                "{}".format( name ) 
                )
            ]
        botton = name
        lys+=ly
    
    lys += [
        to_skip( of=layers[1], to=layers[-2], pos=1.25),
    ]
    return lys

def invisible_box(name, botton, offset="(0,0,0)", width=2, height=40, depth=40, opacity=0.5, caption=""):
    return [
        to_Relu( name=name, offset=offset, to="({}-east)".format(botton), width=width, height=height, depth=depth, opacity=opacity),
        draw_half_down_broken( of=botton, to=name),
        draw_cross("({}-east)".format(name))
    ]

def to_dashed (of, to):
    return [
        draw_dashed_nearnortheast(of, to),
        draw_dashed_nearsoutheast(of, to),
        draw_dashed_farnortheast(of, to),
        draw_dashed_farsoutheast(of, to)
    ]

def conv_block( name, s_filer=256, n_filer=64, offset="(1,0,0)", to="(0,0,0)", width=2, height=40, depth=40, opacity=0.5, caption=""):
    return [
        to_Conv( name=name, s_filer=s_filer, n_filer=n_filer, offset=offset, to=to, width=width, height=height, depth=depth, caption='\makebox[0pt]{\shortstack[c]{Conv2d\\\BN\\\Relu}}'),
        to_BacthNorm(name=(name+'_batchnorm'), offset="(0,0,0)", to="({}-east)".format(name), width=width/3, height=height, depth=depth, caption=''),
        to_Relu(name=name+"_relu", offset="(0,0,0)", to="({}-east)".format(name+'_batchnorm'), width=width/4, height=height, depth=depth, opacity=opacity, caption=''),
    ]

def conv_batchnorm( name, s_filer=256, n_filer=64, offset="(1,0,0)", to="(0,0,0)", width=2, height=40, depth=40):
    return [
        to_Conv( name=name, s_filer=s_filer, n_filer=n_filer, offset=offset, to=to, width=width, height=height, depth=depth, caption='\makebox[0pt]{\shortstack[c]{Conv2d\\\BN}}'),
        to_BacthNorm(name=(name+'_batchnorm'), offset="(0,0,0)", to="({}-east)".format(name), width=width/3, height=height, depth=depth),
    ]

def apply_policy_map( name, botton, s_filer=256, n_filer=64, offset="(0,0,0)", width=2, height=40, depth=40, opacity=0.5, caption=""):
    pass

def se_block (name, s_filer=256, n_filer=64, offset="(1,0,0)", to="(0,0,0)", width=2, height=40, depth=40):
    # global pool
    # dense
    # relu
    # dense
    # add 
    pass

def policy_head( name, botton, s_filer=256, n_filer=64, offset="(0,0,0)", width=2, height=40, depth=40, opacity=0.5, caption=""):
    policy_conv_1_name = name + '_conv_1'
    policy_conv_1 = conv_block(name=policy_conv_1_name, 
                             s_filer=s_filer, 
                             n_filer=n_filer, 
                             offset=offset, 
                             to="({}-east)".format(botton),
                             width=width,
                             height=height,
                             depth=depth
                            )
    connection_1 = draw_half_up( of=botton, to=policy_conv_1_name)
    botton = policy_conv_1_name

    policy_conv_2_name = name + '_conv_2'
    policy_conv_2 = to_Conv(name=policy_conv_2_name, 
                       s_filer=s_filer, 
                       n_filer=80, 
                       offset="(2.4,0,0)", 
                       to="({}-east)".format(botton), 
                       width=width * 2, 
                       height=height, 
                       depth=depth,
                       caption='\makebox[0pt]{\shortstack[c]{Conv2d}}'
                       )
    connection_2 = to_connection( 
        "{}".format(botton), 
        "{}".format(policy_conv_2_name), 
    )
    botton = policy_conv_2_name

    # # reshape and policy map
    # policy_reshape_name = name + '_reshape'
    # policy_reshape = to_FC(name=policy_reshape_name, 
    #                    s_filer=1, 
    #                    n_filer=8*8*80, 
    #                    offset="(2,0,0)", 
    #                    to="({}-east)".format(botton), 
    #                    width=width * 6, 
    #                    height=width * 1.5 * 1.5, 
    #                    depth=width * 1.5 * 1.5,
    #                    caption='\makebox[0pt]{\shortstack[c]{Reshape/Flatten}}'
    #                    )    
    # connection_3 = draw_dashed( 
    #     "{}".format(botton), 
    #     "{}".format(policy_reshape_name), 
    # )
    # botton = policy_reshape_name

    # policy map + softmax
    policy_map_name = name + '_policy_map'
    policy_map = to_FC_softmax(name=policy_map_name, 
                       s_filer=1, 
                       n_filer=1858, 
                       offset="(2.3,0,0)", 
                       to="({}-east)".format(botton), 
                       width=width * 7, 
                       height=width * 1.5 * 1.5, 
                       depth=width * 1.5 * 1.5,
                       caption='\makebox[0pt]{\shortstack[c]{ \\\ \\\ \\\ Reshape\\\PolicyMap\\\Softmax}}'
                       ) 

    connection_3 = draw_dashed( 
        "{}".format(botton), 
        "{}".format(policy_map_name), 
    )

    # connection_4 = to_connection( 
    #     "{}".format(botton), 
    #     "{}".format(policy_map_name), 
    # )
    botton = policy_map_name


    # final output
    policy_output_name = name + '_output'
    policy_output = to_FC(name=policy_output_name, 
                       s_filer=1, 
                       n_filer=1, 
                       offset="(2.3,0,0)", 
                       to="({}-east)".format(botton), 
                       width=width * 1.5 * 1.5, 
                       height=width * 1.5 * 1.5, 
                       depth=width * 1.5 * 1.5,
                       caption='\makebox[0pt]{\shortstack[c]{Policy Output\\\Qh6}}'
                       ) 

    connection_5 = to_connection_dashed( 
        "{}".format(botton), 
        "{}".format(policy_output_name), 
    )
    botton = policy_output_name


    # label = create_label(policy_conv_1_name, policy_output_name, caption)
    # output_img_name = "output_img"
    # output_img = to_output('chess.png', off='3', to="({}-east)".format(botton), width=8, height=8, name=output_img_name)

    return [*policy_conv_1, connection_1, policy_conv_2, *connection_2, policy_map, connection_3, policy_output, connection_5]
    

def value_head(name, botton, s_filer=256, n_filer=64, offset="(0,0,0)", width=2, height=40, depth=40, opacity=0.5, caption=""):
    value_conv_1_name = name + '_conv_1'
    value_conv_1 = conv_block(name=value_conv_1_name, 
                             s_filer=s_filer, 
                             n_filer=n_filer, 
                             offset=offset, 
                             to="({}-east)".format(botton),
                             width=width,
                             height=height,
                             depth=depth
                            )
    connection_1 = to_connection_broken( of=botton, to=value_conv_1_name)

    botton = value_conv_1_name


    # reshape and policy map
    # value_flatten_name = name + '_flatten'
    # value_flatten = to_FC(name=value_flatten_name, 
    #                    s_filer=1, 
    #                    n_filer=2048, 
    #                    offset="(2.5,0,0)", 
    #                    to="({}-east)".format(botton), 
    #                    width=width * 8, 
    #                    height=width * 1.5 * 2, 
    #                    depth=width * 1.5 * 2,
    #                    caption='\makebox[0pt]{\shortstack[c]{Flatten}}'
    #                    )    
    # connection_2 = draw_dashed( 
    #     "{}".format(botton), 
    #     "{}".format(value_flatten_name), 
    # )
    # botton = value_flatten_name

    # dense_1
    value_dense1_name = name + '_dense1'
    value_dense1 = to_FC(name=value_dense1_name, 
                       s_filer=1, 
                       n_filer=128, 
                       offset="(2.5,0,0)", 
                       to="({}-east)".format(botton), 
                       width=width * 5.5, 
                       height=width * 1.5 * 2, 
                       depth=width * 1.5 * 2,
                       caption='\makebox[0pt]{\shortstack[c]{Flatten\\\Fully Connected}}'
                       )    
    connection_2 = draw_dashed( 
        "{}".format(botton), 
        "{}".format(value_dense1_name)
    )
    # connection_3 = to_connection( 
    #     "{}".format(botton), 
    #     "{}".format(value_dense1_name), 
    # )

    botton = value_dense1_name    


    # dense_2
    value_dense2_name = name + '_dense2'
    value_dense2 = to_FC_softmax(name=value_dense2_name, 
                       s_filer=1, 
                       n_filer=3, 
                       offset="(2.5,0,0)", 
                       to="({}-east)".format(botton), 
                       width=width * 4.5, 
                       height=width * 1.5 * 2, 
                       depth=width * 1.5 * 2,
                       caption='\makebox[0pt]{\shortstack[c]{Fully Connected\\\Softmax}}'
                       )    
    connection_4 = to_connection( 
        "{}".format(botton), 
        "{}".format(value_dense2_name), 
    )
    botton = value_dense2_name  


    # final output
    value_output_name = name + '_output'
    value_output = to_FC(name=value_output_name, 
                       s_filer=1, 
                       n_filer=1, 
                       offset="(2.5,0,0)", 
                       to="({}-east)".format(botton), 
                       width=width * 1.5 * 2, 
                       height=width * 1.5 * 2, 
                       depth=width * 1.5 * 2,
                       caption='\makebox[0pt]{\shortstack[c]{Value Output\\\80\% to win}}'
                       ) 

    connection_5 = to_connection_dashed( 
        "{}".format(botton), 
        "{}".format(value_output_name), 
    )
    botton = value_output_name

    return [*value_conv_1, connection_1, value_dense1, connection_2, value_dense2, connection_4, value_output, connection_5]


def block_Res_2( name, botton, s_filer=256, n_filer=64, offset="(0,0,0)", width=2, height=40, depth=40, opacity=0.5, caption=""):
    lys = []
    # Conv block 1, with bn and relu
    conv1_name = name + '_conv_1'
    res_conv_block1 = conv_block(name=conv1_name, 
                                 s_filer=s_filer, 
                                 n_filer=n_filer, 
                                 offset=offset, 
                                 to="({}-east)".format(botton),
                                 width=width,
                                 height=height,
                                 depth=depth
                                 )
    connection_1 = to_connection( 
                "{}".format(botton), 
                "{}".format(conv1_name) 
                )
    botton = conv1_name

    # Conv block 2, with bn only
    conv2_name = name + '_conv_2'
    res_conv_block2 = conv_batchnorm(name=conv2_name, 
                                       s_filer=s_filer, 
                                       n_filer=n_filer, 
                                       offset="(1,0,0)", 
                                       to="({}-east)".format(botton), 
                                       width=width, 
                                       height=height, 
                                       depth=depth
                                       )
    connection_2 = to_connection( 
            "{}".format(botton), 
            "{}".format(conv2_name) 
            )
    botton = conv2_name

    # se block
    se_name = name + '_se'
    se_block = to_SE(name=se_name, 
                     s_filer=s_filer, 
                     n_filer=n_filer, 
                     offset="(1,0,0)", 
                     to="({}-east)".format(botton), 
                     width=width, 
                     height=height, 
                     depth=depth,
                     caption='\makebox[0pt]{\shortstack[c]{SE}}'
                     )

    connection_3 = to_connection( 
            "{}".format(botton), 
            "{}".format(se_name) 
            )
    
    botton = se_name

    # skip connection, not an actual convolutional layer
    skip_name = name + '_skip'
    conv_skip_add = to_Conv(name=skip_name, 
                       s_filer=s_filer, 
                       n_filer=n_filer, 
                       offset="(1,0,0)", 
                       to="({}-east)".format(botton), 
                       width=width, 
                       height=height, 
                       depth=depth,
                       caption='\makebox[0pt]{\shortstack[c]{Add\\\Relu}}'
                       )
    
    add_symbol_name = name + '_add'
    add_conv = to_Add(name=add_symbol_name,
                      offset="(0,0,0)",
                      to="({}-east)".format(skip_name),
                      radius=2.5, opacity=0.6
                     )

    connection_4 = to_connection( 
            "{}".format(botton), 
            "{}".format(skip_name) 
            )

    # relu after addition
    add_relu_name = name + "_add_relu"
    conv_skip_add_relu = to_Relu(name=add_relu_name, 
                            offset="(0,0,0)", 
                            to="({}-east)".format(skip_name), 
                            width=width/4, 
                            height=height, 
                            depth=depth, 
                            opacity=opacity)

    # draw skip connection line
    skip_connection = to_skip( of=conv1_name, to=skip_name, pos=1.25)
    
    lys = [*res_conv_block1, connection_1, *res_conv_block2, connection_2, se_block, connection_3, conv_skip_add, add_conv, conv_skip_add_relu, connection_4, skip_connection]

    return lys


