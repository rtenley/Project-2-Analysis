
# coding: utf-8

# In[5]:


import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import seaborn as sns
import os
my_dir = os.path.join("/", "c:", "Desktop")
os.path.isdir(my_dir)


# In[6]:


pd.__version__


# In[7]:


food = pd.read_csv('C:\Desktop\Chipolte.csv')


# In[ ]:


os.listdir(my_dir)


# In[ ]:


my_path = os.path.join("/", "c:", "Desktop", "Chipolte.csv")
os.path.isfile(my_path)


# In[ ]:


print(my_path)


# In[ ]:


print(my_dir)


# In[ ]:


get_ipython().system('ls')


# In[ ]:


get_ipython().system('DIR')


# In[ ]:


os.path.isfile("Chipolte.csv")


# In[ ]:


os.getcwd()


# In[ ]:


os.listdir('.')


# In[ ]:


os.path.isfile('chipoltle.csv')


# In[ ]:


food = pd.read_csv('chipoltle.csv')


# In[ ]:


food


# In[ ]:


#Converted tsv to csv using Excel and save as.


# In[ ]:


#Calculate the average price of an order.
#Total orders and total price needed.
#Total price / Total orders
#Total orders 1834
#Convert item_price from string to float
food['item_price'] = food['item_price'].str.replace('$', '').astype(float)
x = food.loc[:, 'order_id']
y = food.loc[:, 'item_price']


# In[ ]:


food.dtypes


# In[ ]:


sum(y)


# In[ ]:


sum(y) / 1834 #Average price of an order


# In[ ]:


#Does quantity column have an effect on this calculation?
z = food.loc[:, 'quantity']


# In[ ]:


sum(z)


# In[ ]:


sum(z) / 1834


# In[ ]:


#The average order has 2.7 items ordered.  
#There appears to be a discounted rate for multiple orders of one item.


# In[ ]:


food.loc[food.quantity > 1, 'quantity'].value_counts()


# In[ ]:


food_quantity = food.loc[food.quantity > 1]


# In[ ]:


food_quantity


# In[ ]:


food_quantity.dtypes


# In[ ]:


a = (sum(food_quantity.loc[:, 'item_price']))


# In[ ]:


b = (sum(food_quantity.loc[:, 'quantity']))


# In[ ]:


a / b


# In[ ]:


# The quantity column lowers the average as they are cheaper items, appetizers, drinks, etc.


# In[ ]:


food


# In[ ]:


food.sort_values('item_name')


# In[ ]:


food.loc[:, 'item_name'].value_counts()


# In[ ]:


unique_sodas = food.loc[food['item_name'] == 'Canned Soda', :]


# In[ ]:


unique_sodas1 = food.loc[food['item_name'] == 'Canned Soft Drink', :]


# In[ ]:


unique_sodas.loc[:, 'choice_description'].value_counts()


# In[ ]:


unique_sodas1.loc[:, 'choice_description'].value_counts()


# In[ ]:


#Tried multiple options to combine 'Canned Soda' and 'Canned Soft Drink, but continued to get errors.


# In[9]:


food


# In[ ]:


#Calculate the average number of toppings per burrito
#Ignore quantity column
#Need item_name burrito, chicken burrito, steak burrito, veggie burrito, barbacoa burrito, carnitas burrito
#Will need counts for choice_description for each burrito.


# In[ ]:


burrito_data = food.loc[food['item_name']] = [['burrito', 'Chicken Burrito', 'Steak Burrito', 'Veggie Burrito', 'Barbacoa Burrito', 'Carnitas Burrito', :]]


# In[8]:


choice = food.loc[choice_description].value_counts()

