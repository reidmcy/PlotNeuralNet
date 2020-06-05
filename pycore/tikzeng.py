
import os

def to_head( projectpath ):
    pathlayers = os.path.join( projectpath, 'layers/' ).replace('\\', '/')
    return r"""
\documentclass[border=8pt, multi, tikz]{standalone} 
\usepackage{import}
\subimport{"""+ pathlayers + r"""}{init}
\usetikzlibrary{positioning, shapes}
\usetikzlibrary{3d} %for including external image 
"""

def to_cor():
    return r"""
\def\ConvColor{rgb:yellow,5;red,2.5;white,5}
\def\ConvReluColor{rgb:yellow,5;red,5;white,5}
\def\PoolColor{rgb:red,1;black,0.3}
\def\OpoolColor{rgb:blue,2;green,1;black,0.3}
\def\FcColor{rgb:blue,5;red,2.5;white,5}
\def\FcReluColor{rgb:blue,5;red,5;white,4}
\def\SoftmaxColor{rgb:magenta,5;black,7}   
\def\BatchNormColor{rgb:red,1;black,0.3}
\def\SumColor{rgb:blue,5;red,2.5;white,5}
\def\TestColor{rgb:white,1;black,2;blue,1}
"""

def to_begin():
    return r"""
\newcommand{\copymidarrow}{\tikz \draw[-Stealth,line width=0.8mm,draw={rgb:blue,4;red,1;green,1;black,3}] (-0.3,0) -- ++(0.3,0);}
\newcommand{\brokenmidarrow}{\tikz \draw[-Stealth,line width=0.8mm,draw={rgb:red,1;black,0.3}] (-0.3,0) -- ++(0.3,0);}

\begin{document}
\begin{tikzpicture}
\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=\edgecolor,opacity=0.7]
\tikzstyle{copyconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:blue,4;red,1;green,1;black,3},opacity=0.7]
\tikzstyle{brokenconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:red,1;black,0.3},opacity=0.7]

\tikzset{cross/.style={cross out, draw={rgb:red,1;black,0.3}, minimum size=2*(#1-\pgflinewidth), inner sep=0pt, outer sep=0pt},cross/.default={10pt}}

"""

# layers definition

def to_input( pathfile, to='(-3,0,0)', width=8, height=8, name="temp" ):
    return r"""
\node[canvas is zy plane at x=0] (""" + name + """) at """+ to +""" {\includegraphics[width="""+ str(width)+"cm"+""",height="""+ str(height)+"cm"+"""]{"""+ pathfile +"""}};
"""

# Conv
def to_Conv( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_Add(name, offset="(0,0,0)", to="(0,0,0)", radius=2.5, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Ball={
        name="""+name+""",
        caption="""+ caption +r""",
        fill=\SumColor,
        opacity="""+ str(opacity) +""",
        radius="""+ str(radius) +""",
        logo="""+ "\(+\)" +""",
        }
    };
"""

# Conv
def to_ConvBatchNorm( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        bandfill=\BatchNormColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# def to_ConvBatchNormRelu( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, opacity=0.5, caption=" " ):
#     return r"""
# \pic[shift={ """+ offset +""" }] at """+ to +""" 
#     {RightBandedBox={
#         name="""+ name +""",
#         caption="""+ caption +""",
#         xlabel={{"""+ str(n_filer) +""", }},
#         zlabel="""+ str(s_filer) +""",
#         fill=\ConvColor,
#         bandfill=\BatchNormColor,
#         height="""+ str(height) +""",
#         width="""+ str(width) +""",
#         depth="""+ str(depth) +"""
#         }
#     };


def to_BacthNorm(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+name+""",
        caption="""+ caption +r""",
        fill=\BatchNormColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_Relu(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+name+""",
        caption="""+ caption +r""",
        fill=\ConvReluColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_SE( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption=" " ):
	return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+ name +""",
        caption="""+ caption +""",
        xlabel={{"""+ str(n_filer) +""", }},
        ylabel="""+ str(s_filer) +""",
        fill=\PoolColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
	};
"""

def to_FC( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption=" " ):
	return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+ name +""",
        caption="""+ caption +""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\FcColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
	};
"""

def create_label(edge_a, edge_b, label):
	return r"""
\path ("""+ edge_a +"""-south) edge["Policy Head"',text width=60,text centered, opacity=0, text opacity=1] ("""+ edge_b +"""-south);
"""

def to_output( pathfile, off='0', to='(0,0,0)', width=8, height=8, name="output" ): 
    return r""" 
\node[canvas is zy plane at x="""+ off +"""] (""" + name + """) at """+ to +""" 
{\includegraphics[width="""+ str(width)+"cm"+""",height="""+ str(height)+"cm"+"""]{"""+ pathfile +"""}}; 
"""


def to_FC_softmax( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=2, height=40, depth=40, caption=" " ):
	return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\FcColor,
        bandfill=\SoftmaxColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
	};
"""

# Conv,Conv,relu
# Bottleneck
def to_ConvConvRelu( name, s_filer=256, n_filer=(64,64), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        xlabel={{ """+ str(n_filer[0]) +""", """+ str(n_filer[1]) +""" }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height="""+ str(height) +""",
        width={ """+ str(width[0]) +""" , """+ str(width[1]) +""" },
        depth="""+ str(depth) +"""
        }
    };
"""



# Pool
def to_Pool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+name+""",
        caption="""+ caption +r""",
        fill=\PoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# unpool4, 
def to_UnPool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+ name +r""",
        caption="""+ caption +r""",
        fill=\OpoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""



def to_ConvRes( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=6, height=40, depth=40, opacity=0.2, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(n_filer) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""


# ConvSoftMax
def to_ConvSoftMax( name, s_filer=40, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# SoftMax
def to_SoftMax( name, s_filer=10, offset="(0,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, opacity=0.8, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        xlabel={{" ","dummy"}},
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def draw_half_up( of, to):
    return r"""
    \draw [connection] """ + "({}-north)".format(of) +""" -- node {\midarrow} """ + "({}-north|-{}-west)".format(of, to)  +""" -- node {\midarrow} """ + "({}-west)".format(to) + """ ;
"""

def draw_half_down( of, to):
    return r"""
    \draw [connection] """ + "({}-south)".format(of) +""" -- node {\midarrow} """ + "({}-south|-{}-west)".format(of, to)  +""" -- node {\midarrow} """ + "({}-west)".format(to) + """ ;
"""

def draw_half_down_broken( of, to):
    return r"""
    \draw [brokenconnection] """ + "({}-south)".format(of) +""" -- node {\\brokenmidarrow} """ + "({}-south|-{}-west)".format(of, to)  +""" -- node {\\brokenmidarrow} """ + " ({}-west)".format(to) + """ ;
"""

# https://github.com/HarisIqbal88/PlotNeuralNet/blob/master/examples/VGG16/vgg16.tex
def draw_dashed(of, to):
    return r"""
\draw [densely dashed] 
("""+to+"""-west)++(0, 1.5*.2 * 1.5, 1.5*.2 * 1.5) coordinate(a) -- ("""+of+"""-nearnortheast)
("""+to+"""-west)++(0,-1.5*.2 * 1.5, 1.5*.2 * 1.5) coordinate(b) -- ("""+of+"""-nearsoutheast)
("""+to+"""-west)++(0,-1.5*.2 * 1.5,-1.5*.2 * 1.5) coordinate(c) -- ("""+of+"""-farsoutheast)
("""+to+"""-west)++(0, 1.5*.2 * 1.5,-1.5*.2 * 1.5) coordinate(d) -- ("""+of+"""-farnortheast)

(a)--(b)--(c)--(d)
;
"""

def draw_dashed_nearnortheast(of, to):
    return r"""
\draw [densely dashed]  ("""+of+"""-nearnortheast)   -- ("""+to+"""-nearnorthwest);
"""

def draw_dashed_nearsoutheast(of, to):
    return r"""
\draw [densely dashed]  ("""+of+"""-nearsoutheast)   -- ("""+to+"""-nearsouthwest);
"""

def draw_dashed_farnortheast(of, to):
    return r"""
\draw [densely dashed]  ("""+of+"""-farnortheast)   -- ("""+to+"""-farnorthwest);
"""

def draw_dashed_farsoutheast(of, to):
    return r"""
\draw [densely dashed]  ("""+of+"""-farsoutheast)   -- ("""+to+"""-farsouthwest);
"""

def draw_cross(loc):
    return r"""
\draw """+loc+""" node[cross] {};
"""
def to_connection( of, to):
    return r"""
\draw [connection]  ("""+of+"""-east)    -- node {\midarrow} ("""+to+"""-west);
"""

def to_connection_dashed( of, to):
    return r"""
\draw [densely dashed]  ("""+of+"""-east)    -- node {\midarrow} ("""+to+"""-west);
"""

def to_connection_broken( of, to):
    return r"""
\draw [brokenconnection]  ("""+of+"""-east)    -- node {\\brokenmidarrow} ("""+to+"""-west);
"""

def to_skip( of, to, pos=1.25):
    return r"""
\path ("""+ of +"""-south) -- ("""+ of +"""-north) coordinate[pos="""+ str(pos) +"""] ("""+ of +"""-top) ;
\path ("""+ to +"""-south)  -- ("""+ to +"""-north)  coordinate[pos="""+ str(pos) +"""] ("""+ to +"""-top) ;
\draw [copyconnection]  ("""+of+"""-north)  
-- node {\copymidarrow}("""+of+"""-top)
-- node {\copymidarrow}("""+to+"""-top)
-- node {\copymidarrow} ("""+to+"""-north);
"""

def to_end():
    return r"""
\end{tikzpicture}
\end{document}
"""


def to_generate( arch, pathname="file.tex" ):
    with open(pathname, "w") as f: 
        for c in arch:
            print(c)
            f.write( c )
     


