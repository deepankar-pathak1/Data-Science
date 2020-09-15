#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.array([1,2,3])
print(a)


# In[3]:


print(np.arange(10))


# In[4]:


a = np.arange(100)
get_ipython().run_line_magic('timeit', 'a ** 2')


# In[5]:


# create an array
b = np.array([1,2,3,4])
print(b)


# In[7]:


b.ndim


# In[8]:


b.shape


# In[9]:


len(b)


# In[12]:


# create 2-D array
c = np.array([[1,2,3],[4,5,6]])
print(c)


# In[13]:


c.ndim


# In[14]:


c.shape


# In[15]:


len(c)


# In[18]:


# 3 - D array
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
d


# In[23]:


e.ndim


# In[24]:


e.shape


# In[25]:


len(e) # length will show or return output of first dimension


# In[26]:


# creating numpy array using functions'

a = np.arange(9) # not included 9
print(a)


# In[27]:


b = np.arange(1,10,2) # (start,end,stepsize)
print(b)


# In[28]:


# linear space
c = np.linspace(0,1,6) # (start,end,number of points)
print(c)


# In[29]:


# identical matrix
np.eye(2) # 2 * 2 identical matrix


# In[34]:


np.zeros(3)


# In[35]:


np.zeros((3,3))


# In[36]:


np.ones((3,3))


# In[38]:


np.diag([1,2,3])


# In[39]:


np.random.rand(3) # this is uniformly distributed radom number


# In[40]:


np.random.randn(3) # sample of standard normal number


# In[47]:


a = np.arange(10)
print(a)
print(type(a))
a.dtype


# In[48]:


# we can change the dtype
b = np.arange(10, dtype = "float64")
print(b)


# In[49]:


d = np.array([1+2j,2+4j])
d.dtype


# In[50]:


e = np.array([True, False, True])
e.dtype


# In[51]:


# indexing
a = np.arange(10)
print(a[5])


# In[54]:


a = np.diag([1,2,3])
print(a)
print(a[2][2])


# In[56]:


# we can assign a value
a[2][1] = 99
print(a)


# In[57]:


a = np.arange(10)
print(a)


# In[58]:


a[1:8:3]


# In[64]:


b = np.arange(5)
print(b)
a[5:] = b[::-1]
print(a)


# In[65]:


a = np.arange(10)
print(a)


# In[66]:


b = a[1:9:2]
print(b)


# In[68]:


np.shares_memory(a,b) # here both a and b share same memory(pointing same memory)


# In[69]:


b[0] = 10
print(a)


# In[72]:


a = np.arange(10)
print(a)
b = a[::2].copy()
print(b)
np.shares_memory(a,b) # because here we have created a copy it is deep copy so pointer point two bucktes


# In[75]:


# fancy indexing
# here we do indexing with boolean or integer 

# it creates copies but not views, copeies means deep copy where pointer point different locations

a = np.random.randint(0,20,10)
print(a)


# In[76]:


mask = (a % 2 == 0)
extract = a[mask]
print(extract)


# In[82]:


np.shares_memory(a,extract)


# In[84]:


# indexing with array of integer

a = np.arange(10)
print(a)


# In[85]:


a[[2,2,3,2,3,4]]


# In[ ]:




