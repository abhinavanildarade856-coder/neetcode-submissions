# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2

        sum1 = ""
        sum2 = ""

        while curr1:
            sum1 += str(curr1.val)
            curr1 = curr1.next

        while curr2:
            sum2 += str(curr2.val)
            curr2 = curr2.next

        l3 = int(sum1[::-1]) + int(sum2[::-1])

        arr = [int(x) for x in str(l3)[::-1]]

        head = ListNode(arr[0])
        curr = head

        for val in arr[1:]:
            curr.next = ListNode(val)
            curr =curr.next

        return head
            








