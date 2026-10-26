# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        val1 = ""

        while current:
            val1 = str(current.val) + val1
            current = current.next

        current = l2
        val2 = ""
        while current:
            val2 = str(current.val) + val2
            current = current.next

        print(val1)
        print(val2)
            