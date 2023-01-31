# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        
        if (size - n) == 0:
            head = head.next
            return head
        cur = head
        prev = cur
        index = 0
        
        while index < (size - n):
            prev = cur
            cur = cur.next
            index += 1   
        prev.next = cur.next
        return head