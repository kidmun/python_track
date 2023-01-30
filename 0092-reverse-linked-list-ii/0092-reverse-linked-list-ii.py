# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_prev = left
        cur = head
        index = 0 
        prev = cur
        while index < (left - 1):
            prev = cur
            cur = cur.next
            index += 1
        rev = None
        tail = None
        while left <= right:
            nex = cur.next
            if not rev:
                cur.next = None
                tail = cur
            else:
                cur.next = rev
            rev = cur
            cur = nex
            if left == right:
                if left_prev > 1:
                    prev.next = rev
        
                tail.next = cur
            left +=1
        if left_prev <= 1:
            return rev
        else:
            return head

                
                
                
            
            
            
            
        