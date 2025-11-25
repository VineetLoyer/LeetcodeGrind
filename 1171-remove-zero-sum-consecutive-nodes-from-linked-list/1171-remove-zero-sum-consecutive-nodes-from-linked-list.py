# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        # first pass: build a prefix sum map
        sum_to_node = {}
        cur = dummy
        prefix_sum = 0

        while cur:
            prefix_sum += cur.val
            sum_to_node[prefix_sum] = cur
            cur = cur.next

        #second pass: remove zero sum
        cur = dummy
        prefix_sum = 0
        while cur:
            prefix_sum+=cur.val
            cur.next = sum_to_node[prefix_sum].next
            cur = cur.next
        return dummy.next