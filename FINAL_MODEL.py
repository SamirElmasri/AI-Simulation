# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:30:18 2021

@author: Samir
"""

import numpy as np
import os
os.environ["MODIN_ENGINE"] = "ray"
import modin.pandas as pd
from os import walk
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras import Sequential
import random


#change directory and define training split %
directory = r'C:\Users\Samir\Desktop\Beam Neural Network\matlab'
os.chdir(directory)

print ('directory loaded')

#list the file names
file_names = []
for (dirpath, dirnames, filenames) in walk(directory):
    if filenames == 'logs': 
        pass
    else:
        file_names.extend(filenames)
    break

print ('file names listed')

#create a dataframe
def create_dataframe(file_names):
    list_dataset = {}
    length = []
    for file in file_names:
        list_dataset[file] = pd.read_csv(file, header = None)
        length.append(len(list_dataset[file]))
    return list_dataset, length

#data generator
def generator(train_filess, train_dataset):
    while True:
        for file in train_files:
            inputs = train_dataset[file].iloc[:,:29].to_numpy()
            output = train_dataset[file].iloc[:,30].to_numpy()
        yield inputs, output
        

#split the dataset names and shuffle the the values
random.shuffle(file_names)
training_split = 0.7
train_files_finish = int(len(file_names) * training_split)
train_files = file_names[0:train_files_finish]
validation_files = file_names[train_files_finish:len(file_names)]

print ('file names split')

#create the training dataset in pandas format
train_dataset, batch_size = create_dataframe(train_files)

print ('training data created')


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
model.fit(generator(train_files,train_dataset))