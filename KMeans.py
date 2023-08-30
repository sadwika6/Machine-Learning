# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:24:58 2023

@author: sadwika sabbella
"""

import pandas as pd;

data=pd.read_excel(r"C:\Users\sadwika sabbella\Desktop\pyfh\kmeans1.xlsx")
print(data.head())

data1=data.drop(["ID Tag","Model","Department"],axis=1)

print(data1.head())


from sklearn.cluster import KMeans
km=KMeans(n_clusters=2,init='k-means++',n_init=10)
km.fit(data1)

x=km.fit_predict(data1)
print(x)

data["cluster"]=x

data1=data.sort_values(['cluster'])
print(data1)

data1.to_csv('kmeanspredicted.csv')