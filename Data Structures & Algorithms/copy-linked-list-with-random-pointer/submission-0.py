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
            return None

        curr = head
        while curr:
            nextCurr = curr.next
            node = Node(curr.val, None, curr.random)
            curr.next = node
            node.next = nextCurr
            curr = nextCurr

        copyHead = head.next
        curr = head
        
        while curr:
            copyCurr = curr.next
            if copyCurr.random:
                copyCurr.random = copyCurr.random.next
            curr = copyCurr.next

        curr = head
        while curr:
            copyCurr = curr.next
            nextOrig = copyCurr.next
            curr.next = nextOrig
            if nextOrig:
                copyCurr.next = nextOrig.next
            else:
                copyCurr = None
            curr = nextOrig
        return copyHead
