# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        prev = head
        cur = head.next
        prev.next = None
        res = None
        count = 0
        ans = None
        while cur:
            if cur.val == prev.val:
                count += 1
            else:
                if count < 1:
                    if not res:
                        
                        res = ans = prev
                    else:
                        res.next = prev
                        res = res.next
                      
                prev = cur
                count = 0
                
            
            cur = cur.next
            prev.next = None
            
        if prev and count < 1:
            if not res:
                res = ans = prev
            
                res.next = None
            else:
                if res.val != prev.val:
                    res.next = prev
                    res = res.next
                    res.next = None

            
        
        
        return ans
            
            
            
                
                
     

                
            
   
        return head