# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        
        cur = head
        while cur:
            prev = cur.next
            cur.next = ans
            ans = cur
            cur = prev
        return ans
        