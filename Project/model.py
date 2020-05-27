#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import keras  
from keras.datasets import mnist 
from keras.models import Model 
from keras.layers import Dense, Input
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten 
from keras import backend as k 


# In[2]:


(x_train, y_train), (x_test, y_test) = mnist.load_data()


# In[3]:


img_rows, img_cols=28, 28

if k.image_data_format() == 'channels_first': 
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols) 
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols) 
    inpx = (1, img_rows, img_cols) 

else: 
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1) 
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1) 
    inpx = (img_rows, img_cols, 1) 


# In[4]:


x_train = x_train.astype('float32') 
x_test = x_test.astype('float32') 
x_train /= 255
x_test /= 255


# In[5]:


#Converting to one-hot encoded vector
y_train = keras.utils.to_categorical(y_train) 
y_test = keras.utils.to_categorical(y_test) 


# In[6]:


#layers of the cnn model
inpx = Input(shape=inpx) 
layer1 = Conv2D(32, kernel_size=(3, 3), activation='relu')(inpx) 
layer2 = Conv2D(64, (3, 3), activation='relu')(layer1) 
layer3 = MaxPooling2D(pool_size=(3, 3))(layer2) 
layer4 = Dropout(0.5)(layer3) 
layer5 = Flatten()(layer4) 
layer6 = Dense(250, activation='sigmoid')(layer5) 
layer7 = Dense(10, activation='softmax')(layer6) 


# In[7]:


model = Model([inpx], layer7) 
model.compile(optimizer=keras.optimizers.Adadelta(), loss=keras.losses.categorical_crossentropy, metrics=['accuracy']) 
model.fit(x_train, y_train, epochs=3, batch_size=128) 


# In[8]:


score = model.evaluate(x_test, y_test, verbose=0) 
print('loss=', score[0]) 
print('accuracy=', score[1]) 


# In[ ]:


#Model weights are saved to HDF5 format. 
#This is a grid format that is ideal for storing multi-dimensional arrays of numbers.

#The model structure can be described and saved using JSON format.


# In[9]:


# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
    
# serialize weights to HDF5
model.save_weights("model.h5")


# In[ ]:




