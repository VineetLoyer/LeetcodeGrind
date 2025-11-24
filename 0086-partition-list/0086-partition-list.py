# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        more_head = ListNode(0)
        less = less_head
        more = more_head
        current = head
        while current:
            if current.val<x:
                less.next = current
                less = less.next
            else:
                more.next = current
                more = more.next
            current = current.next
        more.next = None
        less.next = more_head.next
        return less_head.next
