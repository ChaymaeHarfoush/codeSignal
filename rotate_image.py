# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 19:59:40 2018

@author: Chaymae
"""

from copy import deepcopy
def rotateImage(a):

    rot=deepcopy(a)
    for x in range(0,len(a)):
        for y in range(len(a)-1,-1,-1):
            rot[x][len(a)-1-y]=a[y][x]
    return rot


a=[[1,2,3], 
 [4,5,6], 
 [7,8,9]]
print(rotateImage(a))


def rotate_Image(a):
    return list(zip(*reversed(a)))

print(rotate_Image(a))