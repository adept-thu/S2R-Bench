import os
path = "/home/liulin/workspace/Dual-Radar-master/data/dual_radar_plus/robo3d/fog/val/label"
files = os.listdir(path)
for file in files:
    with open('/home/liulin/workspace/Dual-Radar-master/data/dual_radar_plus/robo3d/fog/ImageSets/val.txt', 'a') as f:
        file = file.split('.')[0]
        f.write(file+'\n')
print(files)