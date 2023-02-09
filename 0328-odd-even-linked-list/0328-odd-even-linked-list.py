# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast = head
        odd_h = odd_t = head
        even_h = even_t = head.next
        print(head)
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                odd_t.next = fast
                odd_t = fast
                if not fast.next:
                    even_t.next = None       
                else:
                    even_t.next = fast.next
                    even_t = fast.next
        odd_t.next = even_h        
        return odd_h
            
              
        
           
                
                
        
                
            
  
        