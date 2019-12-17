# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:05:56 2019

@author: Helen
"""
    
#save img into binary image folder
import numpy as np
import cv2
import glob
import os
import cv2 as cv

images=[]

# GT_path: to read all image have extension are .jpg
#outpath1: address for DT_db
#outpath1_2: adress for groundtruth after convert from RGBtoBW
#filename1: list of filename of image in groundTruth_pre folder

#GT_path = glob.glob("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_training/*.jpg") 
#outpath1 = ("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_db")
#outpath1_2 = ("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Training/GT_nom")
#filenames1 = os.listdir("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_training")
#
#train_path = glob.glob("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\imageJPG\\*.jpg") 
#filenames2 = os.listdir("E:\\A_paper_thesis\\Datasets\\LungCancer_ncku\\imageJPG")
#outpath2 = ("E:\\A_paper_thesis\Datasets\\LungCancer_ncku\\imgJPG_1")

"""
1. convert RGB to binary image for ground truth and change extension to .png for ground truth
"""
#for i, img in enumerate(GT_path):
#    filename1 = filenames1[i]
#    filename1 = filename1[:-4]
#    filename1_2 = filenames1[i]
#    filename1_2 = filename1_2[:-4]
##    filename = outpath + '\\' + filename + '.png'#os.path.join(outpath, filename + '.png')
#    filename1 = os.path.join(outpath1, filename1 + '.png')
#
#    print(filename1)
#    n = cv.imread(img,2)
#    img = np.asarray(n)
#    ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # convert img to binary
#    nom_img=bw_img/255 # nomolize binary image to 0 and 1
#    
#    filename1_2 = os.path.join(outpath1_2, filename1_2 + '.png')
#    cv2.imwrite(filename1, bw_img)
#    cv2.imwrite(filename1_2, nom_img)

"""
2. Make the extension of Lung images to be come consistent with .jpg. But for Lung dataset, this part is not necessary
"""   
#for i, img in enumerate(train_path):
#    filename2 = filenames2[i]
#    filename2 = filename2[:-4]
##    filename = outpath + '\\' + filename + '.png'#os.path.join(outpath, filename + '.png')
#    filename2 = os.path.join(outpath2, filename2 + '.jpg')
#    print(filename2)
#    n = cv.imread(img)
#    img = np.asarray(n)
#
#    print('i: {}'.format(i))
#    cv2.imwrite(filename2, img)
    
"""
3. Change extension for test image from .jpg to .png
"""
    
test_pathA = glob.glob("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testA/combine_pre/*.jpg")
filenamesA = os.listdir("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testA/combine_pre")
outpathA = ("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testA/combine_nom")

for i, img in enumerate(test_pathA):
    filenameA = filenamesA[i]
    filenameA = filenameA[:-4]
    filenameA = os.path.join(outpathA, filenameA + '.png')
    n = cv.imread(img,2)
    img = np.asarray(n)
    ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # convert img to binary
    nom_img=bw_img/255 # nomolize binary image to 0 and 1
    

    cv2.imwrite(filenameA, nom_img)

    
test_pathB = glob.glob("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testB/combine_pre/*.jpg")
filenamesB = os.listdir("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testB/combine_pre")
outpathB = ("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testB/combine_nom")

for i, img in enumerate(test_pathB):
    filenameB = filenamesB[i]
    filenameB = filenameB[:-4]

    n = cv.imread(img,2)
    img = np.asarray(n)
    ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # convert img to binary
    nom_img=bw_img/255 # nomolize binary image to 0 and 1
    
    filenameB = os.path.join(outpathB, filenameB + '.png')
    cv2.imwrite(filenameB, nom_img)


    
    