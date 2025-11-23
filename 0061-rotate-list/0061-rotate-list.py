# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #edge cases:
        if not head or not head.next or k==0:
            return head
        
        n = 1
        tail = head 
        while tail.next:
            tail=tail.next # finding the tail
            n+=1 # count the total number of nodes in LL 
        k = k%n #if LL length is 5, and rotate = 12 -> it would be same as rotating by k=2.
        if k==0:
            return head
        tail.next = head
        new_tail = head
        for _ in range(n-k-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head