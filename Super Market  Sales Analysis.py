#!/usr/bin/env python
# coding: utf-8

# # Import Basic Libraries

# In[1]:


import numpy as np
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Load the dataset
df=pd.read_csv("supermarket_sales - Sheet1.csv")


# In[3]:


df.head()


# # Exploratory Data Analysis

# In[4]:


df.shape


# In[5]:


df.columns


# **cogs stands for cost of good sale**

# In[6]:


#check for null values
df.isnull().sum()


# In[7]:


df.describe().T


# In[8]:


df.info()


# In[9]:


#convert 'Date' column datatype into int
df['Date']


# In[10]:


df['Day']=pd.to_datetime(df['Date']).dt.day
df['Month']=pd.to_datetime(df['Date']).dt.month
df['Year']=pd.to_datetime(df['Date']).dt.year


# In[11]:


#drop the "Date" column
df.drop(columns='Date',inplace=True)


# In[12]:


df.head(2)


# In[13]:


#Convert The 'Time column datatype to int'
df["Time"].unique()


# In[14]:


df['Hour']=pd.to_datetime(df['Time']).dt.hour
df['Minutes']=pd.to_datetime(df['Time']).dt.minute


# In[15]:


#drop the Time column
df.drop(columns='Time',inplace=True)


# In[16]:


df.info()


# In[17]:


df.head(2)


# # In which month the 'gross income' was maximum

# In[18]:


df.groupby(['Month'])["gross income"].max().reset_index()


# **In January and Feburary the gross income was high**

# # Which Products were sold in Maximum Quantity with respect to Month

# In[19]:


df.groupby(["Product line","Month"])['Quantity'].size().reset_index()


# **Electronic accessories : Maximum Quantity sold "62" in Feburary**
#     
# **Fashion accessories    : Maximum Quantity sold "64" in January**
#     
# **Food and beverages     : Maximum Quantity sold "62" in Feburary**
#     
# **Health and beauty      : Maximum Quantity sold "57" in March**
#     
# **Home and lifestyle     : Maximum Quantity sold "63" in March**
#     
# **Sports and travel      : Maximum Quantity sold "70" in January**

# # On Which features "Tax5%" Depends

# In[20]:


#Finding the correlation among integral variables
df.corr()


# In[21]:


#Heatmap of variables
plt.figure(figsize=(15,10))
sns.set(font_scale=1.5)
heatmap=sns.heatmap(np.round(df.corr(),2),annot=True,linecolor='white')
heatmap.set_title('Correlation Heatmap Between Variables',fontsize=20);


# **'Tax5%' depends on 'gross income ' and "Quantity"**

# # What is the Relation Between 'Tax5%' and  'gross income'

# In[22]:


plt.figure(figsize=(12,8))
sns.set(font_scale=2)
sns.scatterplot(x='Tax 5%',y='gross income',data=df)
plt.title('Relation Between Gross income and Tax 5%',fontsize=25);


# **'gross income' and 'Tax5% highly Positive correlated**

# # What kind of relation between "Quantity" and "Tax5%"

# In[23]:


plt.figure(figsize=(12,8))
sns.regplot(x='Quantity',y='Tax 5%',data=df,color='blue')
plt.title('Relation Between Quantity and Tax 5%',fontsize=25)


# **"Quantity"  and 'Tax5% highly Positive correlated**

# In[24]:


#which city has more gross income
df['City'].unique()


# In[25]:


df.groupby(['City'])['gross income'].median()


# **Naypyitaw has more gross income than other**

# # In which year gross income was maximum

# In[26]:


#df.groupby(['Year'])['gross income'].max()


# # What is the mean of rating

# In[27]:


df['Rating'].mean()


# In[28]:


#find mean ratiing and visualize it
plt.figure(figsize=(8,8))
sns.set(font_scale=2)
sns.displot(df['Rating'])
plt.axvline(x=np.mean(df['Rating']),c='red',label="Avg Rating")
plt.show()


# # Which kind of Payment method is mostly used by Male and Females

# In[29]:


df['Gender'].value_counts()


# In[30]:


plt.figure(figsize=(20,10))
sns.set(font_scale=2)
sns.countplot('Gender',data=df,hue='Payment')
plt.show()


# **Females are mostly paying through Cash**
# 
# **Males are mostly paying through Ewallet**

# In[31]:


df.columns


# # Which kind of Payment method is mostly used by Member And Normal people

# In[32]:


df['Customer type'].unique()


# In[33]:


plt.figure(figsize=(20,10))
sns.set(font_scale=2)
sns.countplot('Customer type',data=df,hue='Payment',color='blue')
plt.show()


# **Members are mostly paying through Credit Card**
# 
# **Normal people are mostly paying through Ewallet**

# In[34]:


df['Product line'].unique()


# In[35]:


df['gross income']=df['gross income'].astype(int)


# In[36]:


df.head(2)


# # Which type of products are mostly sold in each city

# In[37]:


plt.figure(figsize=(20,10))
sns.set(font_scale=2)
sns.countplot('Product line',data=df,hue='City')
plt.xticks(rotation=90)
plt.legend(loc='upper left');


# # What is relation between gross income and unit price

# In[38]:


plt.figure(figsize=(7,7))
sns.regplot(x='gross income',y='Unit price',data=df,color='g')
plt.title('Relation Between Unit price and gross income',fontsize=20);


# **Unit price and  gross income are positively correlated**
# 
# **gross income increases with unit price**

# # Which products are mostly purchased by Male And female

# In[39]:


plt.figure(figsize=(20,7))
sns.countplot('Product line',data=df,hue='Gender',color='darkblue')
plt.xticks(rotation=90)
plt.show()


# **Mostly males purchased health and beauty products**
# 
# **Mostly females purchased Fashion accessories**

# # How much members  are in each city

# In[40]:


df.groupby(['City',"Customer type"]).size().reset_index()


# In[41]:


#Count city based on custumer type
plt.figure(figsize=(20,8))
sns.countplot('City',data=df,hue='Customer type')
plt.legend(loc="lower left")
plt.show()


# **Maximum members are from Naypyitaw city**

# # On which hour maximum quantities were sold

# In[42]:


#trend of selling products by time
plt.figure(figsize=(8,6))
sns.lineplot('Hour','Quantity',data=df);


# **At 2pm products were sold in maximum quantity**

# In[43]:


plt.figure(figsize=(12,8))
sns.boxplot('Quantity','Product line',data=df)
plt.show()


# # Which product is sold more

# In[44]:


plt.figure(figsize=(15,8))
sns.countplot('Product line',data=df)
plt.xticks(rotation=90)
plt.show()


# **Fashion accessories are sold more than other products**

# # On Each branch which payment method is mostly prefferd by Customers

# In[45]:


#Customers payment in this bussiness
plt.figure(figsize=(15,10))
sns.countplot('Payment',data=df,hue='Branch')
plt.legend(loc='upper right',fontsize=15)
plt.show()


# **On branch 'A' mostly prefferd payment method:Ewallet**
#     
# **On branch 'B' mostly prefferd payment method:Ewallet**
#     
# **On branch 'C' mostly prefferd payment method:Cash**

# # How much maximum rating has each product

# In[46]:


max_rat=df.groupby(['Product line'])['Rating'].max().reset_index()


# In[47]:


max_rat


# In[56]:


plt.figure(figsize=(12,8))
sns.barplot(x='Product line',y='Rating',data=max_rat)
plt.xticks(rotation=90);


# # THANK YOU
