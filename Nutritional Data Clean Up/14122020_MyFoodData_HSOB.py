#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl 
import sklearn 


# In[3]:


try:
    import openpyxl
except:
    get_ipython().system('pip install openpyxl')
    import openpyxl


# In[55]:


data = pd.read_excel('https://www.myfooddata.com/spreadsheets/MyFoodData-Nutrition-Facts-SpreadSheet-Release-1-4.xlsx', header=3, usecols="B:I", engine = 'openpyxl')
data


# In[102]:


#removing the NANs from the dataset for food groups and other values
#data = data[data['Food Group'].notna()]
data_clean = data.dropna(subset=['Food Group', 'Protein (g)','Sugars (g)', 'Fiber (g)'])
data_clean


# In[87]:


# y is the list of food groups 
y = data_clean.iloc[:, 1].values

# x is the labels and nutritional values 
X = data_clean.iloc[:, [0,2,3,4,5,6,7]].values

print(X)
print(y)


# In[88]:


Food_Groups = np.reshape(y, (-1, 1))
Food_Groups


# In[83]:


#inputting to encode but not used 
#Food_Group = (['American Indian', 'Baby Foods', 'Baked Foods', 'Beans and Lentils', 'Beverages', 'Breakfast Cereals','Dairy and Egg Products', 'Fast Foods', 'Fats and Oils', 'Fish', 'Fruits', 'Grains and Pasta', 'Meats', 'Nuts and Seeds', 'Prepared Meals', 'Restaurant Foods', 'Snacks', 'Soups and Sauces', 'Spices and Herbs', 'Sweets', 'Vegetables'])
#Food_Group


# In[99]:


from sklearn.preprocessing import LabelEncoder
labelencoder_Food_Groups_Encoded = LabelEncoder()
Food_Groups[:,0] = labelencoder_Food_Groups.fit_transform(Food_Groups[:,0])
Food_Groups_Encoded = Food_Groups 


# In[101]:


Food_Groups = np.reshape(y, (-1, 1))
Food_Groups


# In[44]:


#creating an array of encoded food categories,
#so food catagories are given numbers rather than names, also made these itnegers not objects
E = y2.astype(np.int32)
y2


# In[45]:


# extracting the encoded numbers back to their original labels for reference 
Food_Group_Numbers = labelencoder_y2.transform(Food_Group)
Food_Group_Numbers


# In[16]:


np.unique(ar=y)


# In[26]:


unique, unique_counts = np.unique(y, axis=0, return_counts=True)
print(np.asarray((unique, unique_counts)))


# In[ ]:




