# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 23:09:15 2018

@author: Chaymae
"""
"""
# Python program to delete a node from linked list
 
# Node class 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Given a reference to the head of a list and a key,
    # delete the first occurence of key in linked list
    def deleteNode(self, key):
         
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None
 
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
 
 
# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
 
print ("Created Linked List: ")
llist.printList()
llist.deleteNode(1) 
print ("\nLinked List after Deletion of 1:")
llist.printList()
"""
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
class linkedList(object):
    def __init__(self):
        self.head=None
    
    def append(self,data):
        
        current=self.head
        
        if current==None:
            self.head=ListNode(data)
            self.head.next=None
            return
        
        while current.next != None:
            current=current.next
        
        new_node=ListNode(data)
        new_node.next=None
        current.next=new_node
    
    def preappend(self,data):
        new_node=ListNode(data)
        new_node.next=self.head
        self.head=new_node
        
    def delete(self,key):
         
        current=self.head
        
        if current==None:
            return
        
        if current.value == key:
            self.head=current.next
        
        while current.next.value != key:
            current=current.next
        
        if current.next==None:
            return
            
        current.next=current.next.next
        
    def printList(self):
        
        current=self.head
        while current != None:
            print(current.value)
            current=current.next
            
mylist=linkedList()
mylist.append(1)
mylist.append(3)
mylist.append(4)        
mylist.append(12)    
mylist.append(5)
mylist.printList()  
print(" ---- " )      
mylist.delete(5)
mylist.printList()  
mylist.preappend(4)
print(" ---- " ) 
mylist.printList()
    
"""
is: will return True if two variables point to the same object, 
==:if the objects referred to by the variables are equal.
this solusion runs on code fights but not here
"""   
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None   
    
def removeKFromList1(l, k):
     
    if l is None:
        return []  
    while l and l.value == k:
        l = l.next
    tmp = l
    while tmp:
        trailer = tmp
        tmp = tmp.next
        while tmp and (tmp.value == k):
            tmp = tmp.next
        trailer.next = tmp
        
    return l  

def removeKFromList2(l, k):
    currentElement = l
    head = l
    prev = None
    
    while currentElement != None:  
        if currentElement.value == k:
            if prev == None:
                currentElement = currentElement.next
                head = currentElement
            else:
                prev.next = currentElement.next
                currentElement = currentElement.next
        else:
            prev = currentElement
            currentElement = currentElement.next
     
    return head
    
print(" ---- " ) 
mylist.printList()   
removeKFromList2(mylist, 3)
print(" ---- " ) 
mylist.printList()
    
    
    
    
    
