# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next

        dummy = ListNode(0)
        dummy.next = prev
        curr = dummy.next
        maxx = float("-inf")

        while curr:
            if curr.val >= maxx:
                maxx = curr.val
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next

        # Reverse the list back
        curr = dummy.next
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


        




        