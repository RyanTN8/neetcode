# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode((l1.val + l2.val) % 10)
        if (l1 and l1.next) or (l2 and l2.next) or ((l1.val + l2.val) // 10 > 0):
            result.next = ListNode((l1.val + l2.val) // 10)
        temp = result.next
        l1 = l1.next
        l2 = l2.next
        while(l1 or l2):
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            val = v1 + v2 + temp.val
            temp.val = val % 10
            if (l1 and l1.next) or (l2 and l2.next) or (val // 10 > 0):
                temp.next = ListNode(val // 10)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result