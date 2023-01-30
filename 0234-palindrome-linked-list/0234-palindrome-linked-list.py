from math import ceil
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        index = 0
        cur = head
        while index < ceil(size/2):
                cur = cur.next
                index += 1
        rev = None
        while cur:
            prev = cur.next
            if not rev:                
                cur.next = None
                rev = cur
                cur = prev
            else:
                cur.next = rev
                rev = cur
                cur = prev
        trav1 = head
        trav2 = rev
        flag = True
        for i in range(size//2):
            if trav1.val != trav2.val:
                flag = False
                break
            trav1 = trav1.next
            trav2 = trav2.next
        return flag
            
                