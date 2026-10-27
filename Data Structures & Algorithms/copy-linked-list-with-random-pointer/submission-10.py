"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        listMap = {None : None}
        current = head
        
        while current:
            node = Node(current.val)
            listMap[current] = node
            current = current.next
        
        current = head

        while current:
            node = listMap[current]
            node.next = listMap[current.next]
            node.random = listMap[current.random]
            current = current.next
        
        return listMap[head]



        