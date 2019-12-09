# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:05:06 2019

@author: Helen
"""
from PIL import Image
import glob
import os

GT_dir = glob.glob("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_bw/*.png") 
filenames = os.listdir("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_bw")

small_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate/GT_small/"
middle_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_main/DataGT_separate/GT_middle/"
large_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate/GT_large/"

#1. save Lung cancer image follow cancer size 

"""
count numbe pixel of Cancer (white pixel): white is (255) in graysale, (255,255,255) in RGB, (1) in binary image
"""

for i, img in enumerate(GT_dir):
  white = 0
  other = 0
  image = Image.open(img)
  filename = filenames[i]
  for pixel in image.getdata():
    if pixel == (1): # ()
        white += 1
    else:
        other += 1
  print('white=' + str(white)+', Other='+str(other))
    
  if white <=200:
    image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate/GT_small/" + filename)
  elif 200< white <=500:
    image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate/GT_middle/" + filename)
  else:
    image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate/GT_large/" + filename)


    

    
    



#







    
              


