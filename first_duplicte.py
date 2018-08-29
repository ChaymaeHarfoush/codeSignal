# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:13:57 2018
@author: Chaymae
"""
"""
your solution cannot pass the time limit. 
"if -a[I] in a " costs O(n) and you use this logic for every element, 
which results in O(n^2)
"""
#def firstDuplicate(a):
#    ans=list()
#    for i in range(len(a)):
#        lst= a[i+1:]
#        if a[i] in lst:
#            ans.append(((lst.index(a[i])+i+1),a[i]))
#    try: return min(ans)[1]
#    except: return -1
#

"""
another solution would be
"""
def firstDuplicate(a):
    
    for i in range(1,len(a)+1,1):
        if a[abs(a[i-1])-1] <0:
                return(abs(a[i-1])) 
        else:
            a[abs(a[i-1])-1]=-a[abs(a[i-1])-1]
    return( -1)
  

print(firstDuplicate([0,8, 1, 0, 0, 0, 0, 1, 0]))