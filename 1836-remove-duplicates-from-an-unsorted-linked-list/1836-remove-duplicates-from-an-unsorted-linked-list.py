# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        #Phase 1 - use hashmap for freq count 
        count = defaultdict(int)
        curr = head
        while curr:
            count[curr.val]+=1
            curr = curr.next
        #Phase 2 - Traverse list again and skip nodes whose value appear more than once.
        dummy = ListNode(0)
        dummy.next = head
        prev,curr = dummy,head
        while curr:
            if count[curr.val]>1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next