# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:56:57 2018
first function had some error in code fights compiler but her not
@author: Chaymae
"""
s= "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"

def firstNotRepeatingCharacter(s):
    count = {}
    for i in s:
        count[i]=count.get(i,0)+1
    for key,value in count.items():
        if value==1:
                return key
    return "_"   
print(firstNotRepeatingCharacter(s))

def fn(s):
  order = []
  counts = {}
  for x in s:
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1 
      order.append(x)
  for x in order:
    if counts[x] == 1:
      return x
  return "_"
print(fn(s))