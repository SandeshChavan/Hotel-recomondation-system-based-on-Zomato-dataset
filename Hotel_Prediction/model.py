#!/usr/bin/env python
# coding: utf-8

# # Zomato hotel's recomondation using KNN model

# In[79]:


#Importing the required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import spatial
import operator




#Reading the data from the file
data=pd.read_csv(r'Zomato.csv')
data=data[0:1000]





#Viewing the imported data
data.head()




#Dropping unnecessary columns
data=data.drop(columns={'url','address','reviews_list','menu_item','dish_liked','phone','listed_in(type)','listed_in(city)'})


# In[83]:


#Renaming the columns
data=data.rename(columns={'name':'Name','online_order':'Online','book_table':'BookTable','rate':'Rate','votes':'Votes','location':'Location','rest_type':'RestType','cuisines':'Cuisines','approx_cost(for two people)':'Cost'})


# In[84]:


#Handling the null values in Cuisines and Type
data.Cuisines=data.Cuisines.replace(np.nan,'UnknownCuisine')
data.RestType=data.RestType.replace(np.nan,'UnknownRestType')


# ## FEATURE ENGINEERING

# In[85]:


#Check values of Location attribute
locList=list(data.Location.unique())


# In[86]:


#Handling the Rest Type attribute
Type=list(data.RestType)
uniqueType=[]
for ele in Type:
    subList=ele.split(',')
    for eleSub in subList:
        eleSub=eleSub.strip()
        if eleSub not in uniqueType:
            uniqueType.append(eleSub)


# In[87]:


#Handling the Rest Type attribute
Cuisines=list(data.Cuisines)
uniqueCuisines=[]
for ele in Cuisines:
    subList=ele.split(',')
    for eleSub in subList:
        eleSub=eleSub.strip()
        if eleSub not in uniqueCuisines:
            uniqueCuisines.append(eleSub)


# In[88]:


#Creating the final dataset
df=pd.DataFrame()
df=data


# In[89]:


#Dummy encoding the columns
df=df.drop(columns={'Location','RestType','Cuisines'})
for types in uniqueType:
    df[types]=np.nan
for cuisines in uniqueCuisines:
    df[cuisines]=np.nan


# In[90]:


dfLoc=pd.get_dummies(data['Location'])


# In[91]:


df=df.fillna(0)


# In[92]:


#Handling the RestType Attributes
for index in data.index:
    ele=data.loc[index]['RestType']
    subList=ele.split(',')
    for eleSub in subList:
        eleSub=eleSub.strip()
        df[eleSub][index]=1
        


# In[93]:


#Handling the RestType Attributes
for index in data.index:
    ele=data.loc[index]['Cuisines']
    subList=ele.split(',')
    for eleSub in subList:
        eleSub=eleSub.strip()
        df[eleSub][index]=1
        


# In[94]:


df.BookTable=df.BookTable.eq('Yes').mul(1)
df.Online=df.Online.eq('Yes').mul(1)


# In[95]:


df.Rate=df.Rate.replace('NEW','0/5')
df.Rate=df.Rate.replace(0,'0/5')


# In[96]:


for index in df.index:
    df['Rate'][index]=float(df['Rate'][index].split("/")[0])


# In[97]:


df.Cost=df.Cost.apply(lambda x: x.replace(',',''))


# In[98]:


df.Cost=df.Cost.astype('int')


# In[99]:


#Final featured and preprocessed dataset
df=pd.concat([df,dfLoc],axis=1)


# In[100]:


df.Rate=df.Rate.astype('float')


# In[101]:


df


# In[102]:


df.iloc[:,85:]


# In[103]:


df.head(1)
data.loc[0][86:]


# In[104]:


testList=list(df.loc[0])
print(len(testList[0:]))


# In[105]:


# Function to calculate distances between movies
def ComputeDistance(a, b):
    OnlineA= a[0]
    OnlineB = b[1]
    BookTableA = a[1]
    BookTableB = b[2]
    RateA = a[2]
    RateB= b[3]
    VotesA= a[3]
    VotesB = b[4]
    CostA=a[4]
    CostB=b[5]#Proper
    RestTypeA=a[5:25]
    RestTypeB=b[6:26]#Proper
    CuisineA=a[26:86]
    CuisineB=b[27:87]
    LocationA=a[84:]
    LocationB=b[85:]
    Online=abs(OnlineA-OnlineB)
    BookTable=abs(BookTableA-BookTableB)
    Rate=abs(RateA-RateB)
    Votes=abs(VotesA-VotesB)
    Cost=abs(CostA-CostB)
    RestType=spatial.distance.cosine(RestTypeA,RestTypeB)
    Cuisine=spatial.distance.cosine(CuisineA,CuisineB)
    Location=spatial.distance.cosine(LocationA,LocationB)
    return Online + BookTable + Rate + Votes + Cost + RestType + Cuisine + Location


# In[106]:



def getNeighbors(a, K):
    distances = []
    for index in df.index:
        dist = ComputeDistance(list(a), list(df.loc[index]))
        distances.append((df['Name'][index], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors






