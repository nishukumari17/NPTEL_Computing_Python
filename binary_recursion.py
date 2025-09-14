# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 12:37:30 2025

@author: Nishu
"""
#l=list x =element
def binary_search(l,x,start,end):
    #base case:1 element
    if(start==end):
        if( l[start]==x):
            return start
        else:
            return -1 # element not found
    else:
        #divide the array into halves
        mid=int((start+end)/2)
        if(l[mid]==x):
            return mid
        #left half
        elif l[mid]>x:
            return binary_search(l,x,start,mid-1)
        #right half
        else:
            return binary_search(l,x,mid+1,end)
        
l=[1,3,4,7,8,12,34,56,77,99,100,129]
x=int(input("Enter the element you want to search: "))
index=binary_search(l,x,0,len(l)-1)
if(index==-1):
    print(x, " Not found") 
else:
    print(x," is found at position ",index+1)           
    