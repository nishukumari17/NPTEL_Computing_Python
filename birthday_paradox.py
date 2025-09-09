# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 21:48:38 2025

@author: Nishu
"""

import random
import datetime
year=random.randint(1990,2015)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("leap year")
else:
    print("Not a leap year")