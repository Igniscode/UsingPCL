import my_objloader as objl
import pcl
import numpy as np
from vtk import *

tmp_obj = objl.OBJ("E:/CloudMethod/Origin/000.obj")
cloud = pcl.PointCloud()
cloud.from_array(np.array(tmp_obj.vertices, dtype=np.float32))
fil = cloud.make_statistical_outlier_filter()

fil.set_mean_k(500)
fil.set_std_dev_mul_thresh(1.0)




