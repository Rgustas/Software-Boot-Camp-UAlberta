
# coding: utf-8

# In[1]:

import numpy


# In[7]:

inarray = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print  inarray.shape


# In[16]:

a = numpy.array([[1,2,3,4],[5,6,7,8],(9,10,11,12)])
#escape characters \n
print "our whole array is\n", a
print "the shape is", a.shape
#rows then collumns 


# In[17]:

#square brackets for lists and indexing
#0,0 is at the upper left 
a[1,1]


# In[18]:

a[1,3]


# In[23]:

a[0,:2]
# up to but not including the last value named


# In[24]:

a[0,:2].mean()


# In[38]:

a[0:2,0:3].sum()


# In[39]:

a[0:2,0:3]


# In[42]:

a[0,:].max()


# In[44]:

a.max(axis=1).mean()


# In[45]:

maxes = a.max(axis=1)
maxes.mean()


# In[49]:

maxes = inarray.max(axis=1)
print maxes


# In[50]:

print maxes.mean()


# In[74]:

maxes[0:10].max(axis=2)


# In[ ]:




# In[ ]:




# In[72]:

inarray[-10:].max(axis=1)


# In[76]:

from matplotlib import pyplot as plt

get_ipython().magic(u'matplotlib inline')

image = plt.imshow(inarray)
plt.show(image)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



