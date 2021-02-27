#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Wholesale_Spend = pd.read_csv('Wholesale customers data .csv', header=None, skiprows=1)


# In[2]:


Wholesale_Spend


# In[3]:


# extracting spending on fresh and milk columns as an array 
X = Wholesale_Spend.iloc[:,2:4].values
X


# In[4]:


Fresh = X[:,0]
Milk = X[:,1]

import numpy as np
import matplotlib.pyplot as plt
plt.scatter(Fresh,Milk, s=2)


# In[82]:


#Mean = np.mean(X)
#Milk_Mean = np.mean(Milk)

#Fresh_SD = np.std(Fresh)
#Milk_SD = np.std(Milk)

#Fresh_distfrommean = abs(Fresh - Fresh_Mean)
#Milk_distfrommean = abs(Milk - Milk_Mean)

#max_dev = 2 

#not_fresh_out = Fresh_distfrommean < max_dev * Fresh_SD

#no_outliers_fresh = Fresh[not_fresh_out]


# In[5]:


#normalising
X = X / np.linalg.norm(X)


# In[84]:


#def reject_outliers(X, m = 2.):
#    d = np.abs(X - np.median(X))
#    mdev = np.median(d)
#    s = d/mdev if mdev else 0.
#    return data[s<m]


# In[7]:


#removing data which falls out of range
threshold = 0.1 
has_outlier = np.any(X > threshold , axis = 1)
X = X[~has_outlier]
X


# In[15]:


Fresh = X[:,0]
Milk = X[:,1]
plt.scatter(Fresh,Milk,s=2)


# In[16]:


# deciding on clusters 
k = 3
centroids = []
for a in range(k):
    rn = np.random.randint(0,len(X))
    centroids.append(X[rn])
    
centroids = np.array(centroids)


# In[17]:


plt.scatter(centroids[:,0], centroids[:,1], marker = '*', s = 300, c = 'red')
plt.scatter(Fresh,Milk,s=3, c='black')


# In[ ]:


#create a clusters array, need a zero for every row in dataset 
clusters = np.zeros(len(X))
prev_clusters = None 
#loop over every data point in the length and calc dist 
#assign point to its closest centroid based on d 
while True: 
    for i in range(len(X)):
# lowest dist 
        low_d = np.inf
#distance to cnetroid for a cluster j 
        for j in range(k):
            d = np.linalg.norm(X[i]-centroids[j], ord=2)
            if d < low_d:
                low_d = d
                best_clust = j
#this data point goes to its best cluster 
        clusters[i] = best_clust 
# update centroids based on this assesment 
#array for each point in a centroid
    k_points = []
    for i in range(k): 
        k_points.append([])
#loop over and go to cluster for dp 
    for i in range(len(X)):
        k_points[int(clusters[i])].append(X[i])
# new avg calc, centroid is the mean 
    for i in range(k):
        centroids[i] = np.mean(k_points[i], axis=0)
# cehack for conversion 
    converge = (clusters==prev_clusters).all()
    print("Have we converged?" + str(converge))
    if converge:
        break
        
    prev_clusters = np.copy(clusters)


# In[ ]:


fig, ax = plt.subplots()
colours = ['r','g','b']
for i in range(k):
    points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
    ax.scatter(points[:, 0], points[:, 1], s=2, c=colours[i])
ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=100, c='black')


# In[ ]:




