# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:29:38 2018
Tow pointers technique
@author: Chaymae
"""

a= [1, 2, 3]
b= [10, 20, 30, 40]
v= 50
def sumOfTwo(a, b, v):
    a=sorted(a)
    b=sorted(b)  
    i=0
    j=len(b)-1

    while (i<=len(a)-1 and j>=0):
        if a[i]+b[j]>v:
            j-=1
        elif a[i]+b[j]<v:
            i+=1
        else:
            return  True
    return False

print(sumOfTwo(a, b, v))
 
    
    
    
    