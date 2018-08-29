# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 22:19:43 2018

@author: Chaymae
"""

from timeit import default_timer as timer
"""
def climbingStairs1(n):

    if n<3:
        return n
    return climbingStairs1(n-1)+climbingStairs1(n-2)
start = timer()       
print(climbingStairs1(38))
start = timer()
print(start-end)
"""
"""
def climbingStairs2(n):
    data={}
    if n<3:
        return n
    elif n not in data:
        data[n]=climbingStairs(n-1)+climbingStairs(n-2)        
    return int(data[n])
        
start = timer()       
print(climbingStairs2(38))
end = timer()
print(end - start)
"""
"""
def climbingStairs3(n):
    data=[0]*n
    if n<3:
        return n
    if data[n-1] == 0:
        data[n-1]=climbingStairs3(n-1)+climbingStairs3(n-2)   
    return data[n-1]
    
start = timer()       
print(climbingStairs3(38))
end = timer()
print(end - start)
"""
"""
the best one in timing 
"""

def climbingStairs4(n):
    if n<=3:
        return n
    data=[0]*(n+1)
    data[0]=0
    data[1]=1
    data[2]=2
    data[3]=3
    for i in range(4,n+1,1):
        data[i]=data[i-1]+data[i-2]
    return data[n]
    
start = timer()       
print(climbingStairs4(38))
end = timer()
print(end - start)

