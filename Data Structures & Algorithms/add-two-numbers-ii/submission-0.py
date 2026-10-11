# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2

        sum1 = ""
        sum2 = ""

        while cur1:
            sum1 += str(cur1.val)
            cur1 = cur1.next

        while cur2:
            sum2 += str(cur2.val)
            cur2 = cur2.next

        l3 = int(sum1) + int(sum2)

        arr= [int(x) for x in str(l3)]

        head  = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next


        return head




