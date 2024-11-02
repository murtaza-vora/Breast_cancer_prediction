#!/usr/bin/env python
# coding: utf-8

# In[7]:


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Activation
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import SeparableConv2D
from tensorflow.keras.utils import to_categorical
import random
from keras import backend as K


# In[1]:


class Murtaza:
  @staticmethod
  def build(width, height, depth, classes):
    model = Sequential()
    inputshape = (height, width, depth)
    chandim =-1
    if K.image_data_format() =='channels_first':
      inputshape = (depth,height,width)
      chandim =1
    model.add(SeparableConv2D(32,(3,3), padding = 'same',input_shape = inputshape))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis = chandim))
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Dropout(0.25))

    model.add(SeparableConv2D(64,(3,3), padding = 'same'))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis = chandim))
    model.add(SeparableConv2D(64,(3,3), padding = 'same'))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis = chandim))
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Dropout(0.25))

    model.add(SeparableConv2D(128,(3,3), padding = 'same'))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis = chandim))
    model.add(SeparableConv2D(128,(3,3), padding = 'same'))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis = chandim))
    model.add(SeparableConv2D(128,(3,3), padding = 'same'))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis = chandim))
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.25))

    model.add(Dense(classes))
    model.add(Activation('softmax'))

    return model


# the concept of chandim ,
# if the inputshape is (height, width, depth) which is predefined by us then chandim = -1(to access channel which is last column)
# 
# if backend engine uses channelfirst formater then change input shape to (depth , height, width) hence now channel will be 1 column thus chandim =1

# In[ ]:





# In[ ]:




