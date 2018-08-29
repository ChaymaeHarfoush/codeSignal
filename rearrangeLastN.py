# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):

    if not l or n==0:
        return l
    tail= cur = l
    lenght=1
    while tail.next is not None:
        lenght +=1
        tail= tail.next
    if lenght==n:
        return l
    stp=lenght-n-1
    for s in range(stp):
        cur=cur.next
    tail.next,cur.next,l=l,None,cur.next
    return l
