# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 19:59:02 2025

@author: Nishu
"""

for i in range(1,51):
    if(i%5==0 and i%3==0):
        print(str(i)+"=fizzbuzz")
    
    else:   
        if(i%5==0):
            print(str(i)+"=buzz")
        else:
            if(i%3==0):
                print(str(i)+"=fizz")
           
            else:
                print(i)