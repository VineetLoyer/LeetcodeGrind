# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 1. Calculate Length (n)
        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next
        # Helper to merge two sorted lists(l1,l2) and return (head,tail)
        def merge(l1:ListNode, l2:ListNode) -> (ListNode,ListNode):
            dummy = ListNode(0)
            tail=dummy
            while l1 and l2:
                if l1.val<=l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            while tail.next:
                tail = tail.next
            return dummy.next,tail
        # Main iterative bottom-up loop
        dummy = ListNode(0)
        dummy.next = head
        step = 1
        while step<n:
            curr = dummy.next
            tail = dummy
            while curr:
                l1 = curr
                l1_tail = l1
                for _ in range(step-1):
                    if l1_tail:
                        l1_tail = l1_tail.next
                if not l1_tail:
                    tail.next = l1
                    break
                
                l2 = l1_tail.next
                l1_tail.next = None
                l2_tail = l2
                for _ in range(step-1):
                    if l2_tail:
                        l2_tail = l2_tail.next
                next_curr = None
                if l2_tail:
                    next_curr = l2_tail.next
                    l2_tail.next = None
                merged_head,merged_tail = merge(l1,l2)
                tail.next = merged_head
                tail = merged_tail
                curr = next_curr
            step*=2
        return dummy.next