# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode(3)
        
        trav = ans
        while list1 or list2:
            if not list1:
                while list2:
                    trav.next = list2
                    trav = trav.next 
                    list2 = list2.next
                break
            if not list2:
                while list1:
                    trav.next = list1
                    trav = trav.next
                    list1 = list1.next
                break
            
            if list1.val == list2.val:
                trav.next = list1
                trav = trav.next
         
                list1 = list1.next
               
            elif list1.val > list2.val:
                trav.next = list2
                trav = trav.next
                list2 = list2.next
            else:
                trav.next = list1
                trav = trav.next
                list1 = list1.next
           
        return ans.next
                
      
            
        