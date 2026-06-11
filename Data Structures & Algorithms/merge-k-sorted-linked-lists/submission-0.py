# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if not list1:
                return list2
            if not list2:
                return list1

            if list1.val < list2.val:
                nextNode = list1.next
                result = list1
                list1 = nextNode
            else:
                nextNode = list2.next
                result = list2
                list2 = nextNode
            
            head = result

            while list1 and list2:
                if list1.val < list2.val:
                    nextNode = list1.next
                    result.next = list1
                    result = list1
                    list1 = nextNode
                else:
                    nextNode = list2.next
                    result.next = list2
                    result = list2
                    list2 = nextNode        

            if list1 and not list2:
                result.next = list1
            elif list2 and not list1:
                result.next = list2

            return head

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                if i == len(lists) - 1:
                    mergedLists.append(lists[i])
                else:
                    mergedLists.append(mergeTwoLists(lists[i], lists[i + 1]))
            lists = mergedLists
        if len(lists) < 1:
            return None
        return lists[0]



