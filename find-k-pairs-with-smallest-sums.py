class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        visited  = set([(0, 0)])
        heap = [(0, (0, 0))]
        ans = []
        while heap and k:
            cur = heappop(heap)
            i = cur[1][0]
            j = cur[1][1]
            ans.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heappush(heap, ((nums1[i+1] + nums2[j]),(i + 1, j)))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heappush(heap, ((nums1[i] + nums2[j + 1]),(i, j + 1)))
            k -= 1
        return ans