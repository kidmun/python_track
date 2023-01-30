# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0 
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        
        cur = head
        prev = None
        i = 0
        rem = n % k
        ans = None
        tail = None
        count = 0
        res = None
        while i < n - rem:
            
            if not ans:
                nex = cur.next
                cur.next = ans
                ans = tail = cur
                cur = nex
            
            else:
                nex = cur.next
                cur.next = ans
                ans = cur
                cur = nex
            
            if count == (k - 1):
                if prev:
                    
                    prev.next = ans
                else:
                    res = ans
                prev = tail
                count = 0
                ans = None
                tail = None
            else:
                count += 1
            i += 1
        if rem != 0:
            index = 0
            trav = res

            while index < (n - rem - 1):
           
                trav = trav.next
                index += 1
            trav.next = cur
                    
                
            
        return res
            