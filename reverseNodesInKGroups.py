# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def covertToList(l):
    lst=[]
    while l :
        lst.append(l.value)
        l=l.next
    return lst
def reverseNodesInKGroups(l, k):
    if k ==1:
        return l
    lst=covertToList(l)
    for start in range (0,len(lst),k):
        subLst=lst[start:start+k]
        if len(subLst) < k:
            return lst
        else:
            lst[start:start+k] =subLst[::-1]
    return lst
