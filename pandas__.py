# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:39:09 2023

@author: sadwika sabbella
"""

import pandas as pd
#a=pd.Series([1,2,3,4])
#print(a)
#a=pd.DataFrame([[1,2,3],[4,5,6]])
#print(a)

#a={'c':[3,4,5],'python':[6,8,9]}
#b=pd.DataFrame(a)
#print(b)

#a=pd.DataFrame([[1,2,3],[4,5,6]],columns=['c','python','java'],index=[5,6])
#print(a)

data=pd.read_csv(r"C:\Users\sadwika sabbella\Desktop\pyfh\IMDB-Movie-Data.csv")
data.head()#first 5 rows are returned
data.head(10)
data.tail
data.shape #dimensions
data.columns
data.index


s=data.append(data) #appends data df to data and store in s
print(data.shape)
print(s.shape)

s.drop_duplicates(inplace=True)#removes duplicates in s
#k=s.drop_duplicates() #duplicates gets removed and saved in k
print(s.shape)


print(data.isna()) #returns whether the cell is empty or not by keeping True/False
print(data['Rank'].describe())#gives the description
print(data.describe())

print(data.isna().sum()) #count of empty spaces/cells

data.dropna(inplace=True)#corresponding row of empty cell gets deleted
print(data.shape)

data=pd.read_csv(r"C:\Users\sadwika sabbella\Desktop\pyfh\IMDB-Movie-Data.csv")
#data.dropna(axis=1,inplace=True) #deletes columns with empty spaces
x=data.dropna(axis=1)
print(x.shape)
print(data.shape)


data=pd.read_csv(r"C:\Users\sadwika sabbella\Desktop\pyfh\IMDB-Movie-Data.csv")
data.drop(['Rank','Rating'],axis=1,inplace=True)#deletes columns
print(data.shape)

data=pd.read_csv(r"C:\Users\sadwika sabbella\Desktop\pyfh\IMDB-Movie-Data.csv")
data.fillna(1,inplace=True)#fills empty spaces with 1
data.isna().sum()


data=pd.read_csv(r"C:\Users\sadwika sabbella\Desktop\pyfh\IMDB-Movie-Data.csv")
data['Metascore'].fillna(data['Metascore'].mean(),inplace=True)#replaces emptyspaces in metascore column with the mean
data.isna().sum()

data['Revenue (Millions)'].fillna(data['Revenue (Millions)'].mean(),inplace=True)
data.isna().sum()

data['Director'].unique()
data['Director'].value_counts()#returns the unique directors


z=data.replace('',0)
data['Rank'].replace(to_replace=1,value=10,inplace=True)#replaces 1 with 10
data.head()

data.loc[1:10]#return first 10 rows-->rows
data.iloc[:,:3]#returns all rows with first 3 columns-->columns and rows

print(data[data['Rating']>8.0].count())#return the number of instances corresponding to each columns where the rating is > 8.0

data[data['Year']==2015].count()#

data[data['Year']==2015].sum()#return the sum of all instances in a column for 2015 released films

data[(data['Year']==2015) & (data['Rating']>8.0)].count()#and

data[(data['Year']==2015) | (data['Rating']>8.0)].count()#or

z=data.sort_values(['Year'])#sort the data bases on Year column
print(z)


import numpy as np
a=np.arange(0,1000)
data['sample']=a#adds a new column sample with values of a

data['Verdict']=data['Rating'].apply(lambda x: 'good' if x>6.0 else 'bad')#add a column verdict is added with values good and bad based on ratings


data['datetime']=pd.date_range('2023-01-01 06:00',periods=1000)#datetime column is added


data['date']=pd.to_datetime(data['datetime']).dt.day

data['month']=pd.to_datetime(data['datetime']).dt.month

