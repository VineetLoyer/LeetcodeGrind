# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total = 0
        curr = head
        while curr:
            total+=1
            curr = curr.next
        node1 = node2 = head
        for _ in range(k-1):
            node1 = node1.next
        for _ in range(total-k):
            node2 = node2.next
        node1.val,node2.val = node2.val,node1.val
        return head