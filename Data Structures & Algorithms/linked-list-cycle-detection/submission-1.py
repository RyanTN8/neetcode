# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        p1 = head.next
        p2 = head.next.next
        while (p1 != p2) and p1 and p2 and p1.next and p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        if p1 == p2:
            return True
        return False