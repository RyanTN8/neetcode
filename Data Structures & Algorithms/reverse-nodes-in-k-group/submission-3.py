# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #go through all the nodes and store every kth node; cut off k-1th node from next
        if k == 1:
            return head
        curr = head
        index = 0
        heads = []
        while curr:
            nextNode = curr.next
            if index % k == 0:
                heads.append(curr)
            elif index % k == k - 1:
                curr.next = None
            if not curr.next:
                t = curr
            curr = nextNode
            index += 1

        #if they're not divisible by k, flag = leave out last bit
        flag = index % k > 0
        #reverse the nodes
        for i in range(len(heads)):
            if i == len(heads) - 1 and flag:
                heads[i] = (heads[i], t)
                continue
            prev = None
            node = heads[i]
            tail = node
            while node:
                nextNode = node.next
                node.next = prev
                prev = node
                node = nextNode
            #prev is new head
            heads[i] = (prev, tail)

        #recombine the nodes
        for i in range(len(heads) - 1):
            heads[i][1].next = heads[i + 1][0]

        return heads[0][0]
            




        




            

