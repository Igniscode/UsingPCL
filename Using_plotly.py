import plotly
plotly.tools.set_credentials_file(username='lucidcode',api_key='eIQqkiYFJYYC01Z7OMoX')
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pcl

cloud = pcl.PointCloud()
cloud._from_ply_file("E:/CloudMethod/Changed/000.ply")

clouds = np.array(cloud.to_array(),dtype=np.float32)

XT = clouds[:,0]
YT = clouds[:,1]
ZT = clouds[:,2]

X = XT[1::10]
Y = YT[1::10]
Z = ZT[1::10]
trace = go.Scatter3d(x = X, y = Y, z = Z, mode='markers',marker=dict(
        color='rgb(127, 127, 127)',
        size=1,
        symbol='cube',
        line=dict(
            color='rgb(204, 204, 204)',
            width=1
        ),
        opacity=0.9
    )
)
data = [trace]
scene = go.Scene(
    xaxis=dict(title='X Axis',autorange=False, range= [-500,500]),
    yaxis=dict(title='Y Axis',autorange=False, range = [-500,500]),
    zaxis=dict(title='Z Axis',autorange=False, range = [0,1000]),

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
py.iplot(fig, filename='Halo')