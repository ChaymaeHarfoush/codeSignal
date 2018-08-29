# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:17:02 2018

@author: Chaymae
"""

dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

def groupingDishes(dishes):
    dct={}
    lst=[]
    for dish in dishes:
    
        main_dish=dish[0]
        
        for ingr in dish[1:]:
            if ingr not in dct:
                dct[ingr]=[main_dish]
            else:
                dct[ingr]=dct[ingr]+[main_dish]
       
    for k,v in dct.items():
        if len(v)>=2:
            v.sort()
            v.insert(0,k)
            lst.append(v)
    
    print(lst)
    lst.sort()
    print("-----")
    print(lst)
    return lst
groupingDishes(dishes)