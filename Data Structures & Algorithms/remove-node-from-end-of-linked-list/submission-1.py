# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        if n == length:
            curr = head.next
            head.next = None
            return curr
        
        length = length - n - 1
        curr = head
        for i in range(length):
            curr = curr.next
        
        prevNode = curr
        nextNode = curr.next.next

        curr.next.next = None
        prevNode.next = nextNode

        return head

        