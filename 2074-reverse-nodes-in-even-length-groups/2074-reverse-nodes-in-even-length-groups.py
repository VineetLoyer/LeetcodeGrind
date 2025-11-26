# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self,head,k):
        prev = None
        curr = head
        count = 0
        while curr and count < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        # prev is new head of the reversed group, head is now the tail
        # curr is the next group's start
        return prev, head, curr


    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        
        group = 1
        curr = head
        prevGroupTail = dummy
        while curr:
            groupSize = group
            actual_count = 0
            temp = curr
            while temp and actual_count < groupSize:
                temp = temp.next
                actual_count+=1
            if actual_count % 2==0:
                revHead, revTail, nextGroupHead = self.reverseLinkedList(curr, groupSize)
                prevGroupTail.next = revHead
                revTail.next = nextGroupHead
                prevGroupTail = revTail
                curr = nextGroupHead
            else:
                # move prevGroupTail to curr, curr to group's end
                for _ in range(actual_count):
                    prevGroupTail = curr
                    curr = curr.next
            group += 1
        return dummy.next