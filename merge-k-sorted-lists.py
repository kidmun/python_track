# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        ans = []
        heapify(ans)
        count = 0
        for i in range(len(lists)):
            if lists[i]:
                heappush(ans, (lists[i].val, i, lists[i]))
        trav = None
        res = None
        while ans:
            cur = heappop(ans)
            if not trav:
                trav = res =cur[2]
            else:
                trav.next = cur[2]
                trav = trav.next
            if cur[2].next:
                heappush(ans, (cur[2].next.val, cur[1], cur[2].next))
        return res