# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 11:03:55 2025

@author: Nishu
"""
"""
fact(3)
===> 3 *fact(2)         ===>3*2=6
    ====>2*fact(1)      ==>2*1=2
        ==>1*fact(0)    ====>1*1=1
                ==>1
"""
def fact(n):
    #sum=1
    #Recursive Version
    #fact(n)=n*fact(n-1)
    #fact(0)=1
    if(n==0):
        return  1 
    else:
        return n*fact(n-1 )
n=int(input("Enter the value of n:"))
if(n<0):
    print("factorial of negative number is not possible")
else:
    result=fact(n)
    print ("Factorial is :", result)    