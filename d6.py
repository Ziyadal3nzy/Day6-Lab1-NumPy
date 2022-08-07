#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[162]:


x = np.ones((3, 3))


# In[163]:


x


# In[160]:


y = np.zeros((3, 3))


# In[161]:


y


# In[164]:


x.dtype


# In[165]:


x = np.array([[1.3, 2.4],[0.3, 4.1]])
print('type = ', x.dtype)
print('number of dimensions = ', x.ndim)
print('shape = ', x.shape)
print('size = ', x.size)


# In[168]:


x+y


# In[107]:


w


# In[166]:


y = np.array([0])


# In[167]:


y


# In[ ]:





# In[ ]:





# In[98]:


np.dot(a,b)


# In[129]:


W = np.arange(12,24).reshape(4,3)
W


# In[149]:


W = np.arange(10,16).reshape(3,2)


# In[150]:


W


# In[151]:


Z = np.array([1,3])


# In[153]:


Z


# In[185]:


for newArray in W:
    print(newArray)


# In[173]:


np.vstack((Z,W))


# In[186]:


newArray.transpose()


# In[180]:


newArray = np.arange(1)
newArray


# In[187]:


newArray = np.array([10,11,12,13,14,15,16])


# In[190]:


newArray.min()


# In[191]:


newArray.max()


# In[192]:


newArray[0]


# In[194]:


newArray[2]


# In[195]:


newArray = np.arange(0, 13)


# In[216]:


newArray


# In[219]:


newArray = np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])


# In[225]:


newArray.reshape(9, 1) Error


# In[ ]:


newArray.reshape(3, 2) Error


# In[ ]:





# In[ ]:




