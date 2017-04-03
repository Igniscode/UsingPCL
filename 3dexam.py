from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pcl

cloud = pcl.PointCloud()
cloud._from_ply_file("E:/CloudMethod/Changed/000.ply")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

clouds = np.array(cloud.to_array(),dtype=np.float32)
# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

XT = clouds[:,0]
YT = clouds[:,1]
ZT = clouds[:,2]
X = XT[1::20]
Y = YT[1::20]
Z = ZT[1::20]
print X,Y,Z
ax.scatter(X, Y, Z , s=0.5 ,c='r')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
