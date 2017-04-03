import plotly.plotly as py
from plotly.grid_objs import Grid, Column
import plotly.graph_objs as go
import pcl
import numpy as np
import time

"""
for i in range(150):
    cloud = pcl.PointCloud()
    if i < 10 :
        num = "00"+str(i)
    elif i < 100 :
        num = "0"+str(i)
    else:
        num = str(i)
    in_file_name = "E:/nRE/08_r/imported/000"+num+".ply"

    cloud._from_ply_file(in_file_name)
    clouds = np.array(cloud.to_array(), dtype=np.float32)

    XT = clouds[:, 0]
    YT = clouds[:, 1]
    ZT = clouds[:, 2]
    X = XT[1::20]
    Y = YT[1::20]
    Z = ZT[1::20]
"""



column_1 = Column([0.5], 'x')
column_2 = Column([0.5], 'y')
column_3 = Column([0.5], 'z')
column_4 = Column([1.5], 'x2')
column_5 = Column([1.5], 'y2')
column_6 = Column([1.5], 'z3')

grid = Grid([column_1, column_2, column_3, column_4])

py.grid_ops.upload(grid, 'ping_pong_grid'+str(time.time()), auto_open=False)

scene = go.Scene(
    xaxis=dict(title='X Axis',autorange=False, range= [0,3]),
    yaxis=dict(title='Y Axis',autorange=False, range = [0,3]),
    zaxis=dict(title='Z Axis',autorange=False, range = [0,3]),
)
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    ),
    scene=scene
)

fig = dict(data=data, layout=layout)

figure = {
    'data': [
        {
            'xsrc': grid.get_column_reference('x'),
            'ysrc': grid.get_column_reference('y'),
            'zsrc': grid.get_column_reference('z'),
            'mode': 'markers',
        }
    ],
    'layout': {'title': 'Ping Pong Animation',
               'scene': scene,
               'updatemenus': [{
                   'buttons': [
                       {'args': [None],
                        'label': 'Play',
                        'method': 'animate'}
               ],
               'pad': {'r': 10, 't': 87},
               'showactive': False,
               'type': 'buttons'
                }]},
    'frames': [
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x2'),
                    'ysrc': grid.get_column_reference('y2'),
                    'mode': 'markers',
                }
            ]
        },
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x'),
                    'ysrc': grid.get_column_reference('y'),
                    'mode': 'markers',
                }
            ]
        }
    ]
}

py.icreate_animations(figure, 'ping_pong'+str(time.time()))