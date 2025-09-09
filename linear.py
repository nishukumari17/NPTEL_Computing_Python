# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 00:02:18 2025

@author: Nishu
"""
def linear_search(n,x):
    element=[]
    for i in range(1,1001):
        element.append(i)
        flag=0
        count=0
    for i in element:
        count+=1
        if(i==x): 
            print("Yes!I found my number at position " +str(i))
            flag=1
            break
    if(flag==0):
        print("Number is not found .")



    print("Number of iteration ",count)