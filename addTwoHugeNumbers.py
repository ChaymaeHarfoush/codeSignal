# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
def addTwoHugeNumbers(a, b):
    a = reverse(a)
    b = reverse(b)

    carry = 0
    result = None

    while a is not None or b is not None or carry > 0:
        raw = ((a.value if a is not None else 0) +
               (b.value if b is not None else 0) +
               carry)

        node = ListNode(raw % 10000)
        node.next = result

        result = node
        carry = raw // 10000

        if a is not None:
            a = a.next
        if b is not None:
            b = b.next

    return result

def reverse(list):
    current = list
    previous = None

    while current is not None:
        previous, current.next, current = current, previous, current.next

    return previous

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
from itertools import zip_longest
def addTwoHugeNumbers(a, b):
    def convert(x):
        temp = []
        while x is not None:
            temp.append(x.value)
            x = x.next
        return(temp)

    la=convert(a)[::-1]
    lb=convert(b)[::-1]
    result=[]
    carry=0
    for x, y in zip_longest(la, lb, fillvalue=0):
        z = x + y + carry
        result.append(z % 10000)
        carry = z // 10000

    while carry:
        result.append(carry % 10000)
        carry = carry // 10000

    return(result[::-1])
