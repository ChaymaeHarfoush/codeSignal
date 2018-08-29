# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 17:39:31 2018

@author: Chaymae
"""
def Duplicate(a):
    list1 = []
    for i in a:
        if i != 0:
            if i in list1:
                return False
            else:
                list1.append(i)
    return True
    
def getsubgrid(startPoint, grid):
    sub=[]
    x1=startPoint[0]
    y1=startPoint[1]
    x2=x1+2
    y2=y1+2
    for col in grid[y1:y2+1]:
        for elem in col[x1:x2+1]:
            sub.append(elem)
    return sub


def sudoku2(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]=='.':
                grid[i][j]=0
                
    #print("check rows")    
    #check rows
    for i in range(1,10,1):
        a=list(map(int,grid[i-1]))
        if Duplicate(a) == False:
            return False
    
       
    #print("check col")
    #check columns
    for i in range(1,10,1):
        b=[grid[j][i-1] for j in range(9)]
        b=list(map(int,b))
        if Duplicate(b) == False:
            return False
    #extract and transform 3*3 sub grid to a list
                
    
    #print("check sub_grid")   
                
    #check 3*3 cell
    for i in range(1,10,1):
        index=[(0,0),(0,3),(0,6),
               (3,0),(3,3),(3,6),
               (6,0),(6,3),(6,6)]
        c=getsubgrid(startPoint=index[i-1],grid=grid)
        c=list(map(int,c))    
        if Duplicate(c) == False:
            return False
    return True

    
grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]   
print(sudoku2(grid))
