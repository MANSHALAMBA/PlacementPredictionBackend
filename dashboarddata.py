# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:55:58 2019

@author: Logan
"""

import math as m
import numpy as np
import pandas as pd

data=pd.read_csv(r'Admission_Predict.csv')
y=data.iloc[:,8:9]
w=data.iloc[:,1:2]
u=data.iloc[:,2:3]
z= y.values.tolist()
k=int(0)
l= list()
for i in z:
    k=k+1
    for j in i:
        l.append(j)
    if k>200:
        break
myString = ','.join(map(str, l))

print(myString)
print('\n')


k=int(0)
z1= w.values.tolist()
l= list()
for i in z1:
    k=k+1
    for j in i:
        l.append(j)
    if k>200:
        break
myString = ','.join(map(str, l))


print(myString)
print('\n')

k=int(0)

z2= u.values.tolist()
l= list()
for i in z2:
    k=k+1
    for j in i:
        l.append(j)
    if k>200:
        break
myString = ','.join(map(str, l))


print(myString)

