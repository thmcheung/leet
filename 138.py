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
        if not head:
            return
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                dic[cur].next = dic[cur.next]
            else:
                dic[cur].next = None

            if cur.random:
                dic[cur].random = dic[cur.random]
            else:
                dic[cur].random = None
            cur = cur.next
        
        return dic[head]