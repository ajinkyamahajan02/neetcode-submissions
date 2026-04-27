# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        node = ListNode(val)

        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def reverseLL(self, node):

        mid = node
        

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev = None
        current = slow.next
        slow.next = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        second_half = prev
        first_half = head

        while first_half and second_half:
            first_half_next = first_half.next
            second_half_next = second_half.next

            first_half.next = second_half
            second_half.next = first_half_next

            first_half = first_half_next
            second_half = second_half_next
            

        
        