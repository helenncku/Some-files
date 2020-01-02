# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:32:08 2019

@author: Helen
"""
import matplotlib.pyplot as plt
import cv2
import numpy as np

maskpath = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/GT_testB/combine_pre/IMG-0017-00201.jpg"
imgpath = "E:/A_paper_thesis/Paper00_ThesisCode/DeepLabv3plus_lungCancer/dataset/LungCancer_mainData/Testing/lung_testB/IMG-0017-00201.jpg"



im = cv2.imread(maskpath)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
imgray = cv2.medianBlur(imgray, ksize=7)

ret, thresh = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print ("number of countours detected before filtering %d -> "%len(contours))
new = np.zeros(imgray.shape)

new = cv2.drawContours(im,contours,len(contours)-1,(0,255,0),1)

#cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
#cv2.imshow('Display',new)

mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[contours[len(contours)-1]],0,255,-1)
pixelpoints = cv2.findNonZero(mask)
cv2.imwrite("masked_image.jpg",mask)

print(len(pixelpoints))
print("type of pixelpoints is %s" %type(pixelpoints))

h,w = mask.shape

im_ori = cv2.imread(imgpath)

cv2.drawContours(im_ori,contours,len(contours)-1,(0,255,0),2)
#cv2.drawContours(im_ori,[contours[len(contours)-1]],0,255,-1)
cv2.imwrite("hello.png",im_ori)
cv2.imshow('results', im_ori)

cv2.waitKey()

