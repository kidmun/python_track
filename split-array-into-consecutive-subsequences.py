class Solution:
    def isPossible(self, nums: List[int]) -> bool:
  
        tails = defaultdict(list)
        for num in nums:
            if tails[num - 1]:
                heappush(tails[num], heappop(tails[num - 1]) + 1)
            else:
                heappush(tails[num], 1)
        for key, li in tails.items():
            if li and li[0] < 3:
                return False
        return True