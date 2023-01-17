# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ""
        trav1 = l1 
        trav2 = l2 
        rem = 0
        while trav1 or trav2:
             
            value = 0
            if trav1:
                value += trav1.val
            if trav2:
                value += trav2.val
            res += str((rem + value) % 10)
            rem = (rem + value) // 10
            if trav1:
                trav1 = trav1.next
            if trav2:
                trav2 = trav2.next
        if rem > 0:
            res += str(rem)
        head = ListNode(res[0])
        trav = head
        
        for i in range(1, len(res)):
            n = ListNode(res[i])
            trav.next = n
        
            trav = trav.next
        
        return head
        