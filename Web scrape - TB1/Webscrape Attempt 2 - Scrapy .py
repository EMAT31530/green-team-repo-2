#!/usr/bin/env python
# coding: utf-8

# In[1]:


# creating a platform 
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
# Show Python version
import platform
platform.python_version()


# In[2]:


# trying to import scrapy 
try:
    import scrapy
except:
    get_ipython().system('pip install scrapy')
    import scrapy
from scrapy.crawler import CrawlerProcess


# In[3]:


#checking import works 
import scrapy


# In[4]:


try:
    import pymongo
except:
    get_ipython().system('pip install pymongo')
    get_ipython().system('pip freeze > requirements.text')
    import pymongo


# In[6]:


#starting a project, creates a number of files and folders that include 
#basic 'boilerplate'
get_ipython().system(' scrapy startproject stack')


# In[10]:


#using items to define storage containers for data being scraped 
# the stackitem inherits item(docs) which has a number of pre-defined objects 
# previouslyy built into scrapy 
class StackItem(scrapy.Item):
    name = scrapy.Field()
    pass


# In[11]:


from scrapy.item import Item, Field 

class StackItem(Item):
    price = Field()
    Product = Field()
    


# In[ ]:


#creating the spider 
from scrapy import Spider 
#name defined the spider name, allowed domains contains the base-URLs for spider to crawl 
# start urls is a list of URLs for spider to start crawling from
class StackSpider(Spider):
    name = "Food"
    allowed_domains = ["groceries.morrisons.com"]
    

