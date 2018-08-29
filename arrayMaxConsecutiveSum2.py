# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 16:33:06 2018

@author: Chaymae
"""

inputArray = [-3, -2, -1, -4]
"""
the first one is searching for the 
sum of contiguous subarray within a 
one-dimensional array of numbers which has the largest sum
if the number is negative just return zero
"""
#max_so_far = 0
#max_ending_here = 0
#
#for ele in inputArray:
#    max_ending_here += ele 
#    
#    if max_ending_here<0:
#        max_ending_here=0
#        
#    if max_ending_here>max_so_far:
#        max_so_far=max_ending_here
#print( max_so_far)
"""
this code returns the largest sum in a subarray even if 
the number is negative
"""
def arrayMaxConsecutiveSum2(inputArray):

    max_so_far = inputArray[0]
    max_ending_here = 0

    for ele in inputArray:
        max_ending_here += ele 

        if max_ending_here<ele:
            max_ending_here=ele

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    return( max_so_far)