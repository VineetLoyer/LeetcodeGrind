# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseLinkedList(self,head,k):
    #     prev = None
    #     curr = head
    #     count = 0
    #     while curr and count < k:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #         count += 1
    #     # prev is new head of the reversed group, head is now the tail
    #     # curr is the next group's start
    #     return prev, head, curr


    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: 1 or 2 nodes only
        if not head or not head.next or not head.next.next:
            return head
        node = head
        group = 1

        while node and node.next:
            group += 1

            # Count the number of nodes in the group
            countNodes = 0
            temp = node.next
            while temp and countNodes < group:
                temp = temp.next
                countNodes += 1

            # Reverse if countNodes is even, otherwise skip
            if countNodes % 2 == 0:
                curr = node.next
                prev = None
                for _ in range(countNodes):
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node
                tail = node.next
                tail.next = curr
                node.next = prev
                node = tail
            else:
                for _ in range(countNodes):
                    node = node.next
        return head