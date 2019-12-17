# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:05:06 2019

@author: Helen
"""

#matplotlib inline

import glob
import os
import shutil

"""
  1. copy all image from each folder in GroundTruthFolder_splitTT to GT_training
"""    
#GT_dir = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\GroundTruthFolder_full") # change the name of folder here (last one)
#GT_training = ("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\GT_training") 
#outpath = ("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\GT_combine")    # GT_training is outpath of 1
#
##1. save Lung cancer image follow gt list: jpg
#count = 0
#
##filenames1 = [word.strip() for word in filenames1] # delete /n for every element
#for i, file in enumerate (GT_dir): #526 filenames1
#  filename1 = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\GroundTruthFolder_full\\" + file)
#  GT_path = ("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\GroundTruthFolder_full\\" + file)
#  for j, imageName in enumerate (filename1):
#    image = os.path.join(GT_path, imageName)
#    shutil.copy(image, outpath)
#    
#  count +=1


"""
2. copy all image from each folder in Lung folder of each student to Lung_combine (image all)
"""
GT_training = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\GT_training")
#GT_testA = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\GT_testA")
#GT_testB = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\GT_testB")
#
#lung_dir = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\Student") # change the name of folder here (last one)
#lung_train = ("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\lung_train")     # GT_training is outpath of 1
##lung_combine = ("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\Lung_combine")
#lung_testA = ("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\lung_testA")
#lung_testB = ("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\lung_testB")
#
#count = 0
##filenames1 = [word.strip() for word in filenames1] # delete /n for every element
#for i, file in enumerate (lung_dir): #526 filenames1
#  filename1 = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\Student\\" + file)
#  for j, file1 in enumerate (filename1):
#    if file1 == "Lung":
#      filename2 = os.listdir("E:/A_paper_thesis/Datasets/LungCancer_ncku/Student/" + file + '/' + file1)
#      
#      for k, file2 in enumerate(filename2):
#        final_name = os.listdir("E:/A_paper_thesis/Datasets/LungCancer_ncku/Student/" + file + '/' + file1 + '/' + file2)
#        Lung_path = ("E:/A_paper_thesis/Datasets/LungCancer_ncku/Student/" + file + '/' + file1 + '/' + file2)
#        
#        for h, lung_name in enumerate(final_name):
##          if lung_name in GT_training:
##            Lung = os.path.join(Lung_path, lung_name)
##            shutil.copy(Lung, lung_train)
#          if lung_name in GT_testA:
#            Lung = os.path.join(Lung_path, lung_name)
#            shutil.copy(Lung, lung_testA)
#          elif lung_name in GT_testB:
#            Lung = os.path.join(Lung_path, lung_name)
#            shutil.copy(Lung, lung_testB)  
#    else:
#      break
#  count +=1

  
"""
3. check the ground match with each image between GT_training and image_training

"""  
#GT_dirs = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\GroundTruth") # change the name of folder here (last one)
        
# 20191207
lung_checked = ("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\lung_train_checked")     # this line will be fixed, no change
lung_train = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\lung_train")
lung_path = ("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\mainData\\lung_train")
#image_dir = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\imageJPG")  

#1. save Lung cancer image follow gt list: jpg
count = 0

#filenames1 = [word.strip() for word in filenames1] # delete /n for every element
for i, filename in enumerate(lung_train): #526 filenames1
  if filename in GT_training: #752 image_dir
    filename = os.path.join(lung_path, filename)
    shutil.copy(filename, lung_checked)
    count += 1











    
              


