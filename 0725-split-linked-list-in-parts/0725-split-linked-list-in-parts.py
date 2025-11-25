# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        N=0
        curr = head
        while curr:
            N+=1 # counting total eleements in LL
            curr = curr.next
        
        part_sizes = [N//k]*k # total sublists
        for i in range(N%k):  # overall elements per list
            part_sizes[i]+=1
        
        result = [] # final output list
        curr  = head
        for size in part_sizes:
            this_head = curr
            for i in range(size-1):
                if curr:
                    curr = curr.next
            if curr:
                next_head = curr.next
                curr.next = None
                curr = next_head
            result.append(this_head)
        return result