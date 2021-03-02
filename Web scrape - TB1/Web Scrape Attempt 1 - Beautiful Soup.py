#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
from bs4 import BeautifulSoup


# In[2]:


# trying to import BS
try:
    import bs4
except:
    get_ipython().system('pip install bs4')
    import BeautifulSoup
from bs4 import BeautifulSoup


# In[13]:


# this code performs an HTTP request to the Morrisons website 
# this is done in order to retrieve the HTML which is stored in page
URL = 'https://groceries.morrisons.com/browse/food-cupboard-102705'
page = requests.get(URL)


# In[14]:


print(page.text)


# In[3]:


# creating a beautiful soup object that takes the HTML content as an input 
# here i am instructing beautiful soup to use the a parser to parse the data import beautifulsoup 

from bs4 import beautifulsoup

URL = 'https://groceries.morrisons.com/browse/food-cupboard-102705'
page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')


# In[ ]:


results = soup.find(id = 'main-content')


# In[ ]:


print(results.prettify())


# In[2]:


import sys
print (sys.path)


# In[18]:





# In[ ]:




