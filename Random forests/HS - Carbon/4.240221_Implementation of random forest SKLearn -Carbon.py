#!/usr/bin/env python
# coding: utf-8

# In[49]:


#importing modules for the implementation
import pandas as pd
import numpy as np
import sklearn


# In[78]:


#pulling the data from the pickled dataset 
nutrition = pd.read_pickle("./nutrition_data_clean.pkl")


# In[82]:


#dropping food group and branded columns as they include a lot of NaNs
nutrition.drop(nutrition.columns[1:3], axis=1, inplace=True)
nutrition


# In[83]:


#dropping any rows where there is NaNs from any the data set 
nutrition = nutrition.dropna()


# In[90]:


#extracting the nutrition data, labelling X as this is the input to the SKlearn algorithm
X = nutrition.iloc[:,10:]
X


# In[92]:


#extracting the greenhouse gas emissions 
y = nutrition.iloc[:,6:7]
y


# In[93]:


#splitting the dataset into a test and training data set, with 20% being used for testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2) #size =0.2 means 80% data is training data, 20% testing


# In[105]:


#importing sklearn algorithm and using it with 2000 trees 
#storing the prediction from the test 
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=2000, random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


# In[104]:


#evaluating the model by checking errors
#generally error decreases slightly as number of trees is increased, converges around 200 trees

from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# In[ ]:




