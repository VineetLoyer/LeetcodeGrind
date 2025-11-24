# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        cur = head
        while cur:
            next_temp = cur.next
            prev = dummy
            while prev.next and prev.next.val<cur.val:
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
            cur = next_temp
        return dummy.next