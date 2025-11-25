# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head # new LL from current list, start with head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next # unlink the duplicate 
            else:
                head = head.next # move to next node
        return res
