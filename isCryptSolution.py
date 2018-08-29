# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:31:40 2018

@author: Chaymae
"""
crypt= ["BAA", 
 "BAA", 
 "CAA"]
solution= [["A","0"], 
 ["B","1"], 
 ["C","2"]]
a=crypt[0]
b=crypt[1]
c=crypt[2]

def encryption(lst,solution):
    encLst=[]
    for letter in lst:
        for encrypt in solution:
            if letter==encrypt[0]:
                encLst.append(encrypt[1])
    return encLst
a=encryption(a,solution)
b=encryption(b,solution)
c=encryption(c,solution)  

if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
            print(False)
else:
    letterA=int("".join(a))
    letterB=int("".join(b))
    letterC=int("".join(c)) 
    if letterA+letterB==letterC:
        print(True)
    else:
        print(False)
            
"""
def encryption(lst,solution):
    encLst=[]
    for letter in lst:
        for encrypt in solution:
            if letter==encrypt[0]:
                encLst.append(encrypt[1])
    return encLst
def isCryptSolution(crypt, solution):    
    a=crypt[0]
    b=crypt[1]
    c=crypt[2]        
    a=encryption(a,solution)
    b=encryption(b,solution)
    c=encryption(c,solution)  
    if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                return( False)
    else:
        letterA=int("".join(a))
        letterB=int("".join(b))
        letterC=int("".join(c)) 
        if letterA+letterB==letterC:
            return(True)
        else:
            return(False)

"""          
            
            
            
            
            
            
