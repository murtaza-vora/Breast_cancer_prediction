#!/usr/bin/env python
# coding: utf-8

# In[1]:


import config_IDC


# In[6]:


#!pip install opencv-python


from imutils import paths


# In[7]:


import random
import shutil
import os


# In[8]:


imagepaths = list(paths.list_images(config_IDC.orig_input_dataset))
random.seed(72)
random.shuffle(imagepaths)
number_of_paths = len(imagepaths)
print("Number of image paths:", number_of_paths)


# In[9]:


i = int(len(imagepaths)*config_IDC.TRAIN_SPILT)
trainpaths = imagepaths[:i]
testpaths= imagepaths[i:]


# In[10]:


i = int(len(trainpaths)* config_IDC.VAL_SPILT)
valpaths = trainpaths[:i]
trainpaths2= trainpaths[i:]


# In[11]:


print(len(testpaths))


# In[12]:


datasets = [
    ('training', trainpaths2, config_IDC.TRAIN_PATH),
    ('validation', valpaths, config_IDC.VAL_PATH),
    ('testing', testpaths, config_IDC.TEST_PATH)
]


# In[13]:


for (dtype, imagepaths, baseOutput)in datasets:
    print("[INFO] building '{} spilt'".format(dtype))
    if not os.path.exists(baseOutput):
        print("[INFO] ' create {} directory'".format(baseOutput))
        os.makedirs(baseOutput)


# In[ ]:





# In[14]:


for inputpath in imagepaths:
    filename= inputpath.split(os.path.sep)[-1]
    label = filename[-5:-4]
    labelpath = os.path.sep.join([baseOutput, label])
    if not os.path.exists(labelpath):
        print("[INFO] ' creating{}' directory".format(labelpath))
        os.makedirs(labelpath)
    p= os.path.sep.join([labelpath, filename])
    shutil.copy2(inputpath,p)


# In[ ]:


for (dtype, imagepaths, baseOutput) in datasets:
    print("[INFO] Building '{} split'".format(dtype))
    if not os.path.exists(baseOutput):
        print("[INFO] Creating {} directory".format(baseOutput))
        os.makedirs(baseOutput)
    
    for inputpath in imagepaths:
        filename = os.path.basename(inputpath)
        label = filename[-5:-4]
        labelpath = os.path.join(baseOutput, label)
        if not os.path.exists(labelpath):
            print("[INFO] Creating {} directory".format(labelpath))
            os.makedirs(labelpath)
        destination_path = os.path.join(labelpath, filename)
        shutil.copy2(inputpath, destination_path)

print("[INFO] Done")



# In[43]:





# In[ ]:




