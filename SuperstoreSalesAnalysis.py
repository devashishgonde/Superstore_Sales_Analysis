#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Display values in floating points format in place of exponential format.
pd.set_option('display.float_format',lambda x:'%.3f'%x)


# In[3]:


#just to ignore warnings
import warnings
warnings.filterwarnings('ignore')


# # Gather and clean data

# In[10]:


df=pd.read_csv('C:\\Users\\Lenovo\\Downloads\\superstore_dataset.csv',encoding='ISO-8859-1')

df.head()


# # Explore the Data

# # 1.Display top 5 rows of the Dataset.

# In[5]:


df=pd.read_csv('C:\\Users\\Lenovo\\Downloads\\superstore_dataset.csv',encoding='ISO-8859-1')

df


# In[13]:


df.head()


# # 2.Check the last 5 Rows of the Dataset.

# In[14]:


df.tail()


# # 3.Find shape of our Dataset (No.of Rows & No. of Columns).

# In[29]:


df.shape


# # 4.Get information about our dataset like Total no. of rows ,Total no. of columns ,Datatypes of each columns & memory requirements.

# In[30]:


df.info()


# # 5.Check the null values in the dataset.

# In[31]:


df.isnull().sum()


# # 6.Check the duplicate date & drop them.

# In[32]:


df.duplicated().any()


# # 7.Get overall statistics about the dataset.

# In[33]:


df.describe()


# # 8.Drop unnencessary Columns

# In[37]:


df.columns


# In[38]:


df.drop(['Order ID','Quantity','Discount'],axis=1)


# # HYPOTHESIS

# # Hypothesis 1: Technology products have the highest the profit margin compared to other products categories.

# In[48]:


cat_profit=df.groupby('Category')['Profit'].sum()
cat_profit.plot(kind='bar')
plt.title('Profit by Category')
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.show()

#conclusion:The hypothesis is supported  as tewchnology products have the highest profit margin of the three categories.


# # Hypothesis 2:The East region has the highest sales compared to other regions.

# In[51]:


reg_sales=df.groupby('Region')['Sales'].sum()
reg_sales.plot(kind='bar')
plt.title("Total sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# The Hypothesis is not supported as the central region has the highest sales.


# # Hypothesis 3:Sales are higher during certain months of the year.

# In[54]:


df['Order Month']=pd.DatetimeIndex(df['Order Date']).month
month_sales=df.groupby('Order Month')['Sales'].sum()
month_sales.plot(kind='line')
plt.title("Total Sales by month")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

#Conclusion:Our hypothesis is supported as sales are higher than during certain months if the year.


# # Hypothesis 4: Orders with same-day shipping have the lowest rate of returned products.

# In[10]:


Total_Orders_by_Shipping_Mode= df.groupby('Ship Mode').size()
Returned_Orders_by_Shipping_Mode=df[df['Profit']<0].groupby('Ship Mode').size()
Returned_per_by_shipping_mode=(Returned_Orders_by_Shipping_Mode/Total_Orders_by_Shipping_Mode)*100
print(Returned_per_by_shipping_mode)
Returned_per_by_shipping_mode.plot(kind='bar')
plt.title("Returned % by shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Return %")
plt.show()

# Hypothesis is supported as orders with same-dayshippig have the lowest rate of returned products.


# # Hypothesis :5 The company's profit is more on weekends than on weekdays.

# In[12]:


df['Order Day']=pd.DatetimeIndex(df['Order Date']).day_name()
Days_sale=df.groupby('Order Day')['Profit'].sum()
Days_sale.plot(kind="bar")
plt.title("Total Profit by the day of the week")
plt.xlabel("Day of the week")
plt.ylabel("Total Profit")
plt.show()

#Conclusion: Hypothesis is supported as company's profit is higher on weekends compared to weekdays.


# In[ ]:




