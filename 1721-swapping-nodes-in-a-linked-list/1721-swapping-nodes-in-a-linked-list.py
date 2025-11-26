# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

    # Two-Pass approach 
        # total = 0
        # curr = head
        # while curr:
        #     total+=1
        #     curr = curr.next
        # node1 = node2 = head
        # for _ in range(k-1):
        #     node1 = node1.next
        # for _ in range(total-k):
        #     node2 = node2.next
        # node1.val,node2.val = node2.val,node1.val
        # return head
    # One-Pass approach
        first = last = head
        # advance first pointer to the kth node from the start
        for _ in range(1,k):
        # start a null_check at first and a last pointer at head
            first = first.next
        null_check = first
        # Move both null_check and last together until null_check hits the end
        while null_check.next:
            last = last.next
            null_check = null_check.next
        # At that point last will be at kth node from the end.
        first.val, last.val = last.val,first.val
        return head