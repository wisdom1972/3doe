#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 13:56:21 2018

@author: Wisdom Zhang, 

Objective: Read PTS-S200 point cloud data into Python, 



1- 读入点云文件
2- 将点云作为数组
3- 画图


"""


from __future__ import print_function
#import csv
import numpy as np
import pandas as pd



#my_matrix = np.loadtxt(open("095927_R-fixed-left.csv","rb"),delimiter=",",skiprows=0)  

#left_plane = np.loadtxt(open("chengjie_3d.txt","rb"),delimiter=",",skiprows=1)  
left_plane = np.loadtxt(open("diandn.asc","rb"),delimiter=" ",skiprows=0)  



plane = pd.DataFrame({'x':left_plane[:,0],'y':left_plane[:,1],'z':left_plane[:,2]})

'''
plane1= pd.DataFrame()

plane1.x = plane.x
plane1.y=plane.y
plane1.z=plane.z-1
'''
        
np.savetxt('new.csv', left_plane, delimiter = ',')  


# x轴的采样点
#x = zhuanzhi[0]
#y= zhuanzhi[1]
#z= zhuanzhi[2]

z_mean = np.mean(left_plane[:,2])



import matplotlib.pyplot as plt

upper_samples = []
lower_samples = []


for x, y, z in left_plane:
    # x_mean 作为判别平面
    if z > z_mean:
        upper_samples.append((x, y, z))
    else:
        lower_samples.append((x, y, z))
 
uppers = np.array(upper_samples)
lowers = np.array(lower_samples)

print("uppers len is:", np.size(uppers)) 
print("lower len is:", np.size(lowers))
print("left_plane descrip:",plane.describe() )
 
# '.'标明画散点图，每个散点的形状是个圆
plt.plot(left_plane[:,2], left_plane[:,0], '.')
plt.plot(left_plane[:,1], left_plane[:,2], '.')



fig = plt.figure('3D scatter plot')
ax = fig.add_subplot(111, projection='3d')

#ax.scatter(x,y,z, c='r', marker='o')
#ax.scatter(lowers[:, 0], lowers[:, 1], lowers[:, 2], c='g', marker='^')


ax.scatter(uppers[:, 0], uppers[:, 1], uppers[:, 2], c='b', marker='o')
ax.scatter(lowers[:, 0], lowers[:, 1], lowers[:, 2], c='g', marker='^')

# 将平面下移动一个单位， 因为点云的Z数据mean是1
#ax.scatter(plane1.x, plane1.y, plane1.z, c='b', marker='^')
 
plt.show()
