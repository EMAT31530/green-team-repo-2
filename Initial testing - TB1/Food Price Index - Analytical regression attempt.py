#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
df = pd.read_csv('Food_price_indices_over_time.csv', header=None)
#encoding='cp1252'


# In[62]:


df


# In[63]:


# extracting spending on year and fpi columns as an array 
X = df.iloc[4:,0:2].values
X


# In[64]:


Month_Year = X[:,0]
Food_Price_Index = X[:,1]


# In[65]:



import matplotlib.pyplot as plt
plt.scatter(Month_Year, Food_Price_Index)
plt.xlabel('Year')
plt.ylabel('Food Price Index')
#plt.xticks(np.arange(min(Month_Year)), max(Month_Year))


# In[70]:


Month_Year = Month_Year.reshape(len(Month_Year),1)
Food_Price_Index = Food_Price_Index.reshape(len(Food_Price_Index),1)
Food_Price_Index


# In[67]:


import numpy as np 

Month_Year = np.hstack((np.ones(shape=(len(Month_Year),1)), Month_Year))     
Month_Year


# In[68]:


ls = np.linalg.inv(Month_Year.T.dot(Month_Year)).dot(Month_Year.T).dot(Food_Price_Index)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




