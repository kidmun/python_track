# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        trav1 = head
        trav2 = trav1
        while trav2:
            if trav2.val != trav1.val:
                trav1.next = trav2
                trav1 = trav2
            trav2 = trav2.next
        trav1.next = trav2
        return head
                
        