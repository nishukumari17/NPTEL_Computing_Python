# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 10:48:03 2025

@author: Nishu
"""

def factorial():
    sum=1
    n=int(input("Enter the number which factorial you want: "))
    for i in range(1,n+1):
        sum=sum*i
    print("Factotrial is :", sum)
    
factorial()