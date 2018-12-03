# -*- coding: utf-8 -*-
import os
#设定文件路径
path='D:\\darknet-master\\data_1\\trainImage'
i=1
txtName = "train_list.txt"
txtpath = "D:\\darknet-master\\data_1\\"
fullpath = txtpath + txtName
file1 = open(fullpath,'w')
#对目录下的文件进行遍历
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        file1.write("D:\\darknet-master\\data_1\\trainImage\\"+file+"\n")
        i+=1
#结束
print ("End")