# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:30:33 2018

@author: Chaymae
"""

rows=  [13, 1, 1, 10]
def rowsToCols(rows):
    lst=[]
    fans=[]
    for numb in rows:
        lst.append("{0:b}".format(numb))

    x=[str(item).zfill(len(rows)) for item in lst]

    for r in range (len(rows)):
        ans=[]
        for c in range (len(rows)):
            ans.append(x[c][r])
        fans.append(int("".join(ans),2))
    return fans
