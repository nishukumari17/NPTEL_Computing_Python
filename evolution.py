# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 14:47:49 2025

@author: Nishu
"""
import random
def evolove(x):
    ind=random.randint(0,len(x)-1)
    p=random.randint(1,100)
    print(p)
    if(p==1):
        if(x[ind]=='0'):
            x[ind]='1'
        else:
            x[ind]='0'
            
with open("dna.txt") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,len(x)-1):
    evolove(x)
print(x)