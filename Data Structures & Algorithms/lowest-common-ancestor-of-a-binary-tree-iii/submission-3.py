"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        hi = set()

        curr1 = p

        while curr1:
            hi.add(curr1)
            curr1 = curr1.parent

        curr2 = q

        while curr2:
            if curr2 in hi:
                return curr2

            curr2 = curr2.parent


        






