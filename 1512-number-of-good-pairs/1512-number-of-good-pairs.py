from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = Counter(nums)
        for key, amount in freq.items():
            val = amount * (amount - 1)//2 
            count += val
        return count
        
        
        
        