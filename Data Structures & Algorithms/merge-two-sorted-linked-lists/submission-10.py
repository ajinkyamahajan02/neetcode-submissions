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


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = LinkedList()

        while list1 and list2:
            if list1.val >= list2.val:
                res.append(list2.val)
                list2 = list2.next
            elif list1.val < list2.val:
                res.append(list1.val)
                list1 = list1.next

        while list1:
            res.append(list1.val)
            list1 = list1.next

        while list2:
            res.append(list2.val)
            list2 = list2.next
        
        return res.head