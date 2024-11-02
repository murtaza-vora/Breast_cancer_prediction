#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[ ]:





# In[1]:


import os


# In[2]:


orig_input_dataset = '/Users/taherrangwala/Desktop'


# In[3]:


BASE_PATH = "/Users/taherrangwala/Desktop/idc"


# In[4]:


TRAIN_PATH= os.path.sep.join([BASE_PATH, 'training'])
VAL_PATH = os.path.sep.join([BASE_PATH, 'validation'])
TEST_PATH = os.path.sep.join([BASE_PATH, 'testing'])


# In[5]:


TRAIN_SPILT = 0.8
VAL_SPILT = 0.1


# In[6]:


print('[info]: configuration complete')


# In[8]:


file_count = sum([len(files) for root, dirs, files in os.walk(orig_input_dataset)])
file_count


# In[2]:





# In[4]:





# In[ ]:





# In[ ]:




