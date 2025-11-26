# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        # Step 1: Reverse the original list
        head = reverse(head)
        
        # Step 2: Perform the plus one operation
        curr = head
        carry = 1
        prev = None
        while curr:
            total = curr.val + carry
            curr.val = total % 10
            carry = total // 10
            prev = curr
            curr = curr.next

        # Step 3: If there's still a carry, add new node
        if carry:
            prev.next = ListNode(carry)

        # Step 4: Reverse the list again to restore order
        return reverse(head)