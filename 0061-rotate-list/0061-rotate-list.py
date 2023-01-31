# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        
        index = 0
        cur = head
        prev = cur
        if size == 0:
            return head
        k = k % size
        if size < 2 or k == 0:
            return head
        while index < (size - k):
            prev = cur
            cur = cur.next
            index += 1
        prev.next = None
        trav = cur
        while trav.next:
            trav = trav.next
        trav.next = head
        head = cur
        return head
            
            
        