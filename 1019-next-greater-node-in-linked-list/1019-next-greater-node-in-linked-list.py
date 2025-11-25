# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        res = [0]*len(vals)
        stack = []
        for i,val in enumerate(vals):
            while stack and val>vals[stack[-1]]:
                idx = stack.pop()
                res[idx] = val
            stack.append(i)
        return res