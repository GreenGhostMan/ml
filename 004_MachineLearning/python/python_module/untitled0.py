#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:41:49 2020

@author: ghostman
"""

from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

df = pd.read_csv('zoo.csv')

from sklearn.model_selection import train_test_split

all_x = df.iloc[:,1:17]
all_y = df.iloc[:,17]

x_train, x_test, y_train, y_test = train_test_split(all_x,all_y)