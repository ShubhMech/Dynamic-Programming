#!/usr/bin/env python
# coding: utf-8

# In[44]:


def mm(arr,i,j,t,min_=1e199):
#     print(min_)
#     min_ = 1e199
    if i>=j:
        return 0
    
    if t[i][j] !=-1:
        return t[i][j]
    
    else:
        for k in range(i,j):
            temp = arr[i-1]*arr[j]*arr[k]+ mm(arr,i,k,t) + mm(arr,k+1,j,t)
            min_ = min(min_,temp)
            
            t[i][j] = min_
            
    return min_


# In[45]:


arr = [50,20,30,40]


# In[52]:


t = [[-1 for i in range(1001)] for j in range(1001) ]


# In[47]:


mm(arr,1,len(arr)-1,t)


# In[48]:


50,20, 20,30, 30,40


# In[49]:


arr = [1, 2, 3, 4, 3]


# In[53]:


mm(arr,1,len(arr)-1,t)


# In[ ]:





# In[ ]:




