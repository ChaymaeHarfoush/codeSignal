
"""
this code is copiedx from
https://github.com/emirot/codefights/blob/master/interviewPractice/traverseTree.py
"""
t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": None,
            "right": None
        },
        "right": None
    }
}

#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    stack = []
    stack.append(t)
    res = []
    if not t:
        return []
    while len(stack):
        new_n = stack.pop(0)
        res.append(new_n.value)
        if new_n.left:
            stack.append(new_n.left)
        if new_n.right:
            stack.append(new_n.right)       
    return res
