import os
import numpy as np
files_dir = "/media/l_space_a/dual_radar/training/robosense/"
files = os.listdir(files_dir)
num = 0
subnum = 0
for file in files:
    num = num+1
    file_dir = files_dir + file
    points = np.fromfile(file_dir, dtype=np.float16).reshape(-1, 4)
    print(file_dir)
    for point in points:
        if (np.any(np.isnan(point))):
            subnum = subnum + 1
            break
            #print("hhhhhhhhh")
print(subnum,num)
'''
import numpy as np
import os
import argparse
# import pypcd
from pypcd import pypcd

import csv
from tqdm import tqdm
import errno


files_dir = "/home/liulin/workspace/Dual-Radar-master/6-clean_data/raw_data/2023-12-15-15-33-51_1_B/rslidar_new_1_B/"
files = os.listdir(files_dir)
for file in files:
    file_dir = files_dir + file
    pc = pypcd.PointCloud.from_path(file_dir)
    np_x = (np.array(pc.pc_data['x'], dtype=np.float32)).astype(np.float32)
    np_y = (np.array(pc.pc_data['y'], dtype=np.float32)).astype(np.float32)
    np_z = (np.array(pc.pc_data['z'], dtype=np.float32)).astype(np.float32)
    np_i = (np.array(pc.pc_data['intensity'], dtype=np.float32)).astype(np.float32)/256
    points_32 = np.transpose(np.vstack((np_x, np_y, np_z, np_i)))
    for point in points_32:
        print(point)
'''