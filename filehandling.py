# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 14:16:04 2025

@author: Nishu
"""

with open("test.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("I am fine")
    
myfile.close()
