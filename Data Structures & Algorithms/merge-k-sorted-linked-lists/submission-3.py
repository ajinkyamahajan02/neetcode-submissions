# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l]

        dummy = ListNode(-1)
        current = dummy

        while lists:
            min_index = 0

            for i in range(len(lists)):
                if lists[i].val < lists[min_index].val:
                    min_index = i

            current.next = lists[min_index]
            current = current.next

            lists[min_index] = lists[min_index].next

            if not lists[min_index]:
                lists.pop(min_index)

        return dummy.next
        