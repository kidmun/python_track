# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        size = 0
        cur = head
        while cur:
            cur =cur.next
            size += 1
        index = 0
        head2 = None
        cur = head
        while index < (size // 2):
            cur = cur.next
            index += 1
            
        while cur:
            prev = cur.next
            cur.next = head2
            head2 = cur
            cur = prev
        i = 0
        ans = 0
       
        while i< (size // 2):
            ans = max(ans, head.val + head2.val)
            head = head.next
            head2 = head2.next
            i += 1
        return ans
            
            
        
        