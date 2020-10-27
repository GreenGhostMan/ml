#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 01:31:14 2020

@author: ghostman
"""
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from skimage.color import rgb2gray
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.feature import hog
from skimage import data, color, feature
import glob
from sklearn.model_selection import train_test_split

def preProcessing(arr):
    arr_pre = []
    for i in range(np.shape(arr)[0]):
        img = cv2.cvtColor(arr[i], cv2.COLOR_BGR2GRAY)
        img = resize(img,(72,72), anti_aliasing=True)
        arr_pre.append(img)
    return arr_pre
    
def loadImage(arr, n, name_of_fruit):
    label = []
    for i in range(n):
        strr = "rgb/"+name_of_fruit+"_"+str(i+1)+"/*.png"
        for file in glob.glob(strr):
            img = plt.imread(file)
            #img = np.asarray(plt_read)
            #img = np.asarray(plt.imread(file))
            arr.append(img)
            label.append(name_of_fruit)
    return arr, label

apple = []
banana= []
lemon = []
lime  = []
orange= []
peach = []
pear  = []

apple, label_apple = loadImage(apple, 5, "apple")
banana, label_banana = loadImage(banana, 4, "banana")
lemon, label_lemon = loadImage(lemon,6,"lemon")
lime,label_lime = loadImage(lime, 4, "lime")
orange, label_orange = loadImage(orange, 4, "orange")
peach, label_peach = loadImage(peach, 3, "peach")
pear, label_pear = loadImage(pear, 3, "pear")


raw_attrib = {'class':['Apple','Banana','Lemon','Lime','Orange','Peach','Pear'],'amount':[np.shape(apple)[0],np.shape(banana)[0],np.shape(lemon)[0],np.shape(lime)[0],np.shape(orange)[0],np.shape(peach)[0],np.shape(pear)[0]]}
attrib = pd.DataFrame(raw_attrib,columns=['class','amount'])

total_x = np.concatenate((apple,banana,lemon,lime,orange,peach,pear))
total_y = np.concatenate((label_apple,label_banana,label_lemon,label_lime,label_orange,label_peach,label_pear))

x_train, x_test, y_train, y_test = train_test_split(total_x,total_y,test_size=0.33, random_state=42)

print("training amount :",x_train.shape[0])
print("testing amount  :",x_test.shape[0])

x_train_pre = preProcessing(x_train)
x_test_pre  = preProcessing(x_test)

print("Finished preprocessing!")

















