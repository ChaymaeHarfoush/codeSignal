# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):

    if l is None:
        return []
    fast=l
    slow=l
    while fast.next!=None:
        #list have even number of elements
        if fast.next.next ==None:
            fast=fast.next
        #list have even number of elements
        else:
            fast=fast.next.next
            slow=slow.next
    #Reverse a linked list starting from slow node
    prev=slow
    cur=slow.next
    while cur is not None:
        next=cur.next
        cur.next=prev
        prev=cur
        cur=next
    head=l
    #testing if the left side is equal to the right side
    if head.value != fast.value:
        return False
    while head is not slow:
        if head.next.value != fast.next.value:
            return False
        head=head.next
        fast=fast.next

    return True
