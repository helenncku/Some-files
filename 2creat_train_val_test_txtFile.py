# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:23:12 2019

@author: Helen
"""

import random
import os

"""
1. creat_txt_file, dont delete it
"""      
WD = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Training/lung_train"
#WD1="E:\\A_paper_thesis\\paper5\\Ford_dataset\\Scraping Data2\\GroundTruth_db"
files1 = [".".join(f.split(".")[:-1]) for f in os.listdir(WD) if os.path.isfile(os.path.join(WD, f))]
with open('train_pre.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in files1)


WD1="E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Training/GT_nom"
files2 = [".".join(f.split(".")[:-1]) for f in os.listdir(WD1) if os.path.isfile(os.path.join(WD1, f))]
with open('groundtruth_pre.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in files2)
    
#
"""
2. split dataset into train and validation txt, dont delete it
"""
c = list(zip(files1,files2))

random.shuffle(c)
train_pre, groundtruth = zip(*c)
    
from math import floor
split = 0.8
split_index = floor(len(train_pre) * split)
training = train_pre[:split_index]
val = train_pre[split_index:]

with open('./LungCancer_mainData/Training/train.txt', 'w') as outfile:
    outfile.writelines(fn + '\n' for fn in training)
with open('./LungCancer_mainData/Training/val.txt', 'w') as outfile:
    outfile.writelines(fn + '\n' for fn in val)
    
"""
3. creat test.txt for each case for evaluate process of each database
"""
A1 = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testA/large"
testA_l = [".".join(f.split(".")[:-1]) for f in os.listdir(A1) if os.path.isfile(os.path.join(A1, f))]
with open('E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/testA_large.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in testA_l)    
    
A2 = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testA/medium"
testA_m = [".".join(f.split(".")[:-1]) for f in os.listdir(A2) if os.path.isfile(os.path.join(A2, f))]
with open('E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/testA_medium.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in testA_m)
    
A3 = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testA/small"
testA_s = [".".join(f.split(".")[:-1]) for f in os.listdir(A3) if os.path.isfile(os.path.join(A3, f))]
with open('E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/testA_small.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in testA_s)
    
B1 = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testB/large"
testB_l = [".".join(f.split(".")[:-1]) for f in os.listdir(B1) if os.path.isfile(os.path.join(B1, f))]
with open('E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/testB_large.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in testB_l)
    
B2 = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testB/medium"
testB_m = [".".join(f.split(".")[:-1]) for f in os.listdir(B2) if os.path.isfile(os.path.join(B2, f))]
with open('E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/testB_medium.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in testB_m)
    
B3 = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testB/small"
testB_s = [".".join(f.split(".")[:-1]) for f in os.listdir(B3) if os.path.isfile(os.path.join(B3, f))]
with open('E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/testB_small.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in testB_s)


"""
4. creat list sample image for inference process, this file we should get .jpg extension also
"""
test_combine = testA_l + testA_m + testA_s + testB_l + testB_m + testB_s
random.shuffle(test_combine)
    
from math import floor
split = 0.03
split_index = floor(len(test_combine) * split)
test_sample = test_combine[:split_index]

with open('./LungCancer_mainData/Testing/test_sample.txt', 'w') as outfile:
    outfile.writelines(fn + '\n' for fn in test_sample)



    
  
    



    
    




