# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:05:06 2019

@author: Helen
"""
from PIL import Image
import glob
import os
import numpy as np

GT_dir = glob.glob("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_nom/*.png") 
filenames = os.listdir("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_nom")

#verySmall_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate5case/GT_verySmall/"
small_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate3case/GT_small/"
middle_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_main/DataGT_separate3case/GT_middle/"
large_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate3case/GT_large/"
#veryLarge_output = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate5case/GT_veryLarge/"

#1. save Lung cancer image follow cancer size 

"""
count numbe pixel of Cancer (white pixel): white is (255) in graysale, (255,255,255) in RGB, (1) in binary image
"""

white =[]
for i, img in enumerate(GT_dir):
  filename=filenames[i]
  whiteP = 0
  other = 0
  image = Image.open(img)
  for pixel in image.getdata():
    if pixel == (1): # ()
        whiteP += 1
    else:
        other += 1
#  print('white=' + str(whiteP)+', Other='+str(other))
  white.append(whiteP) 

  # separet image into differen folder of follow size of cancer 
  if whiteP <=1000:
      image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate3case/GT_small/" + filename)
  elif 1000< whiteP <=3000:
      image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate3case/GT_middle/" + filename)
  else:
      image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate3case/GT_large/" + filename)
      
      
  # separet image into differen 5 folders of follow size of cancer 
  
#  if whiteP <=180:
#      image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate5case/GT_verySmall/" + filename)
#  elif 180< whiteP <=400:
#      image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate5case/GT_small/" + filename)
#  elif 400< whiteP <=1000:
#      image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate5case/GT_middle/" + filename)
#  elif 1000< whiteP <=2000:
#      image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate5case/GT_large/" + filename)
#  else:
#      image.save("E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/GT_separate5case/GT_veryLarge/" + filename)
      
"""
# save image name and number of white pixel into txt file, dont delete below code
"""
#whiteO = np.array(white)
#listfile = np.column_stack((filenames,whiteO))
#np.savetxt("countPixel_Helen.txt", listfile, delimiter=" ", fmt="%s") 








    
              


