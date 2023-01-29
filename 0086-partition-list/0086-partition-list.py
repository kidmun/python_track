# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = None
        before_tail = None
        after_head = None
        after_tail = None
        
        cur = head
        while cur:
            prev = cur.next
            cur.next = None
            if cur.val < x:
                
                if not before_head:
                    
                    before_head = before_tail = cur
                else:                
                    
                    before_tail.next = cur
                    before_tail = cur
                
            else:
                if not after_head:
                    
                    after_head = after_tail = cur
                else:                
                    
                    after_tail.next = cur
                    after_tail = cur
            cur = prev
        if before_head and after_head:
            before_tail.next = after_head
            return before_head
        elif before_head:
            return before_head
        else:
            return after_head
        