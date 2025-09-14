# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 14:18:50 2025

@author: Nishu
"""

"""
Fibonacci sequence:
    0th fibonnaci n0=0
    1st fibonnaci no=1
    
    
    2nd fib no=0+1=1
    3rd fib no=1+1=2
    4th fib no=1+2=3

"""

#To find nth Fibonacci number
def fibonacci(n):
    if(n<2):
        return(n)
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n=int(input("Enter the number whose fibonnaci you want: "))
if(n<0):
    print("Negative number is not allowed")
else:
    num=fibonacci(n)
    print("The fibonacci is :", num)