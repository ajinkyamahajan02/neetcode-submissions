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
        loc_map = {}

        current = head
        while current:
            node = Node(current.val)
            loc_map[current] = node
            current = current.next

        current = head
        while current:
            node = loc_map[current]
            node.next = loc_map.get(current.next)
            node.random = loc_map.get(current.random)
            current = current.next

        return loc_map[head]
        