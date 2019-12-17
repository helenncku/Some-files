# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:41:10 2019

@author: Helen
"""


from PIL import Image
import os
import cv2

""""
check for one image
""""
#white = 0
#other = 0
#img_bn = Image.open("E:\\A_paper_thesis\\Paper00_ThesisCode\\DeepLabv3plus_lungCancer\\dataset\\inference_output\\IMG-0105-00090_mask.png")
#
#for pixel in img_bn.getdata():
#  if pixel == (255,255,255,255): # ()
#        white += 1
#  else:
#        other += 1
#print('white=' + str(white)+', Other='+str(other))
#
##img_nom = cv2.imread("E:\\A_paper_thesis\\Paper00_ThesisCode\\DeepLabv3plus_lungCancer\\dataset\\LungCancer_mainData\\GT_bw\\IMG-0003-00298.png")
#white_nom = 0
#other_nom = 0
#img_nom = Image.open("E:\\A_paper_thesis\\Paper00_ThesisCode\\DeepLabv3plus_lungCancer\\dataset\\LungCancer_mainData\\GT_bw\\IMG-0105-00090.png")
#for pixel in img_nom.getdata():
#    if pixel == (1): # ()
#        white_nom += 1
#    else:
#        other_nom += 1
#print('white_nom=' + str(white_nom)+', Other_nom='+str(other_nom))


""""
check for multiple images
""""


import glob
import numpy as np

GT_dir = glob.glob("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_bw/*.png") 
filenames = os.listdir("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_bw")

small_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate/GT_small/"
middle_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_main/DataGT_separate/GT_middle/"
large_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate/GT_large/"

#1. save Lung cancer image follow cancer size 

"""
count numbe pixel of Cancer (white pixel): white is (255) in graysale, (255,255,255) in RGB, (1) in binary image
"""

white =[]
for i, img in enumerate(GT_dir):
  whiteP = 0
  other = 0
  image = Image.open(img)
  for pixel in image.getdata():
    if pixel == (1): # ()
        whiteP += 1
    else:
        other += 1
  print('white=' + str(whiteP)+', Other='+str(other))
  
  # save image name and number of white pixel into txt file
  white.append(whiteP)
#  whiteP = np.array(white)
#  listfile_temp = np.column_stack((filename, whiteP))
#  listfile.append(listfile_temp)
#  np.savetxt("countPixel_Helen.txt", listfile, delimiter=" ", fmt="%s")

whiteO = np.array(white)
listfile = np.column_stack((filenames,whiteO))
np.savetxt("countPixel_Helen_inference.txt", listfile, delimiter=" ", fmt="%s")  
  # separet image into differen folder of follow size of cancer 