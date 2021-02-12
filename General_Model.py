# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:30:18 2021

@author: Samir
"""
import pandas as pd
import numpy as np
import os
from os import walk
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras import Sequential
import random


directory = r'/Users/user/Downloads/matlab'

os.chdir(directory)
training_split = 0.7

        
file_names = []

for (dirpath, dirnames, filenames) in walk(directory):
    file_names.extend(filenames)
    break

random.shuffle(file_names)
train_files_finish = int(len(file_names) * training_split)
train_files = file_names[0:train_files_finish]
test_files = file_names[train_files_finish:len(file_names)]


#intiate the model
model = Sequential()

#create the input layer
model.add(Dense(29,input_dim = 29, activation = 'relu'))

#nomalise the data
model.add(BatchNormalization())

#hidden layers
model.add(Dense(12, activation = 'relu'))

#output layer
model.add(Dense(1, activation = 'sigmoid'))

#comple and loss function
model.compile(loss = 'mean_squared_error', optimizer = 'adam')

#fit the model
model.fit(generator(train_files) , use_multiprocessing = True , steps_per_epoch = train_files_finish )