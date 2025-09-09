# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 23:45:15 2025

@author: Nishu
"""

def bubble(a):
     n=len(a)
     for i in range(n):
         for j in range(0,n-i-1):
             if(a[j]>a[j+1]):
                 temp=a[j]
                 a[j]=a[j+1]
                 a[j+1]=temp
                 
a=[5,2,6,8,9,1,45]
bubble(a)

for i in a:
    print(i)