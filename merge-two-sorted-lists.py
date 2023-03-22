# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        def trav(list1, list2, ans):
            nonlocal head
            if not list1 and not list2:
                return head
            elif not list1:
                if not head:
                    head = ans = list2
                else:
                    ans.next = list2
                return head
            elif not list2:
                if not head:
                    head = ans = list1
                else:
                    ans.next = list1
                return head
            if list1.val <= list2.val:
                if not head:
                    head = ans = list1
                else:
                    ans.next = list1
                    ans = ans.next
                val = trav(list1.next, list2, ans)
            else:
                if not head:
                    head = ans = list2
                else:
                    ans.next = list2
                    ans = ans.next
                val = trav(list1, list2.next, ans)
            return val
        return trav(list1, list2, None)