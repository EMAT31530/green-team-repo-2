#!/usr/bin/env python
# coding: utf-8

# ## Using sklearn with KNN algorithm to extract classification of foods based on calories and protein contents of certain types of food. 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl 
import sklearn 
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets


# In[2]:


try:
    import openpyxl
except:
    get_ipython().system('pip install openpyxl')
    import openpyxl


# In[3]:


data = pd.read_excel('https://www.myfooddata.com/spreadsheets/MyFoodData-Nutrition-Facts-SpreadSheet-Release-1-4.xlsx', header=3, usecols="B:I", engine = 'openpyxl')


# In[4]:


#removing the NANs from the dataset for food groups and other values
#data = data[data['Food Group'].notna()]
data_clean = data.dropna(subset=['Food Group', 'Protein (g)','Sugars (g)', 'Fiber (g)'])
data_clean


# In[5]:


# extracting fish beans and lentil data points and baked foods
data_FBL = data_clean[data_clean['Food Group'].isin(['Beans and Lentils','Fish','Baked Foods'])]
data_FBL


# In[15]:


# y is the list of food groups 
y1 = data_FBL.iloc[:, 1].values

# extracting protein and fat columns only for FBL not whole data set 
X1 = data_FBL.iloc[:, [2,4]].values

print(y1)


# In[16]:


Food_Groups = np.reshape(y1, (-1, 1))
Food_Groups


# In[17]:


#inputting to encode but not used 
#Food_Group = (['American Indian', 'Baby Foods', 'Baked Foods', 'Beans and Lentils', 'Beverages', 'Breakfast Cereals','Dairy and Egg Products', 'Fast Foods', 'Fats and Oils', 'Fish', 'Fruits', 'Grains and Pasta', 'Meats', 'Nuts and Seeds', 'Prepared Meals', 'Restaurant Foods', 'Snacks', 'Soups and Sauces', 'Spices and Herbs', 'Sweets', 'Vegetables'])
#Food_Group


# In[18]:


from sklearn.preprocessing import LabelEncoder
labelencoder_Food_Groups = LabelEncoder()
Food_Groups[:,0] = labelencoder_Food_Groups.fit_transform(Food_Groups[:,0])
Food_Groups_Encoded = Food_Groups 


# In[19]:


Food_Groups_Encoded = np.reshape(y1, (-1, 1))
Food_Groups_Encoded = Food_Groups_Encoded.astype(np.int32)
Food_Groups_Encoded


# In[20]:


Food_Groups_Encoded = np.reshape(Food_Groups_Encoded, (1,-1))
Food_Groups_Encoded


# In[21]:


#implementing knn using sklearn so 
 #specifying k number of nearest neighbours 
    
n_neighbors = 5

# showing x and y, FBL ptrotein and fat numebrs and y, the target name label 

X = data_FBL.iloc[:, [2,4]].values
y = Food_Groups_Encoded.flatten()

h = 1  # step size in mesh diagram 


# In[22]:


# Create color maps
cmap_light = ListedColormap(['orange', 'cyan', 'cornflowerblue'])
cmap_bold = ListedColormap(['darkorange', 'c', 'darkblue'])

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points protein on x fat on y
    # baked goods is orange, fish is dark blue and beans and lentils is light blue 
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))
    plt.xlabel('Calories per 100g')
    plt.ylabel('Protein(g)')

plt.show()


# In[108]:





# In[107]:





# In[ ]:





# In[ ]:




