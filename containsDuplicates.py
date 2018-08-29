# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:23:56 2018

@author: Chaymae
"""

def containsDuplicates(a):
    return len(set(a)) != len(a)
#return true when there is a duplicate as len(set(a)) != len(A)
#return false when there is no duplicate since both the sets will have same length  
print(containsDuplicates([1,2,3,4,5,6,1]))