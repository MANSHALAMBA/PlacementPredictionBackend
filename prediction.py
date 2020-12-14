# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:04:27 2019

@author: Logan
"""

import math as m
import numpy as np
import pandas as pd


data=pd.read_csv(r'Admission_Predict.csv')
c=data.head()

x=data.iloc[:,[1,2,3,6,7]]
y=data.iloc[:,8:9]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/4,random_state=0)

from sklearn.tree import DecisionTreeRegressor
regr_1 = DecisionTreeRegressor(max_depth=4)
regr_1.fit(x_train,y_train.values.ravel())
#pred1=regr_1.predict(x_test)

aptscore=float(input("")) #variable to calculate aptitude score 
softskills =float(input(""))#variable to calculate softskill score

univrating = int(input(""))
univrating =(5-univrating)
cgpa = int(input(""))
domknlg = float(input(""))



cgpasb=float(0.9)
cgpast=int(1)

cgpapb=float(0.8)

univratingsb=float(0.8)
univratingst=int(1)
univratingpb=float(0.7)

aptweightsb=float(0.7)
aptweightst=float(1)
aptweightpb=float(0.9)

softskillweightsb=float(0.9)
softskillweightst=float(0.8)
softskillweightpb=float(0.7)

domknlgsb=int(1)
domknlgst=float(0.8)
domknlgpb=float(0.6)




predictsb=regr_1.predict([[aptscore*aptweightsb,softskills*softskillweightsb,univrating*univratingsb,cgpa*cgpasb,domknlg*domknlgsb]])

predictsb=float(predictsb*100)

predictst=regr_1.predict([[aptscore*aptweightst,softskills*softskillweightst,univrating*univratingst,cgpa*cgpast,domknlg*domknlgst]])

predictst=float(predictst*100)

predictpb=regr_1.predict([[aptscore*aptweightpb,softskills*softskillweightpb,univrating*univratingpb,cgpa*cgpapb,domknlgpb*domknlg]])

predictpb=float(predictpb*100)

print predictsb
print predictst
print predictpb





