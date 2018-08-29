# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    a=l1
    b=l2
    result=[]
    while (a is not None) :
        if b is None:
            break
        if a.value<b.value:
            result.append(a.value)
            a=a.next

        else:
            result.append(b.value)
            b=b.next
    if a is None:
        while b is not None:
                result.append(b.value)
                b=b.next
        return result
    else:
        while a is not None:
            result.append(a.value)
            a=a.next
        return result
