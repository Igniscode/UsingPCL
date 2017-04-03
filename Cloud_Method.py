import pcl
import my_objloader as objl
import numpy as np

for i in range(150):
    cloud = pcl.PointCloud()
    if i < 10 :
        num = "00"+str(i)
    elif i < 100 :
        num = "0"+str(i)
    else:
        num = str(i)
    in_file_name = "E:/nRE/08_r/000"+num+".obj"
    out_file_name = "E:/nRE/08_r/imported/000"+num+".ply"

    tmp_obj = objl.OBJ(in_file_name)
    cloud.from_array(np.array(tmp_obj.vertices, dtype=np.float32))

#    cloud._from_ply_file(in_file_name)
#    obj_file = obj.OBJ(in_file_name)

    fil = cloud.make_statistical_outlier_filter()
    fil.set_mean_k(500)
    fil.set_std_dev_mul_thresh(1.0)
    fil.filter()._to_ply_file(out_file_name)
#    fil.filter()._to_ply_file("E:/CloudMethod/Changed/000000.ply")
    print "%s is Successfully filtered !! " %in_file_name
