class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ma = max(nums)
        mi = min(nums)
        ma = max(abs(ma), abs(mi))
        ans = ""
        neg = 0
        for num in nums:
            if num < 0:
                neg += 1
        for i in range(int.bit_length(ma)):
            count = 0
            for num in nums:
                if num < 0:
                    num = abs(num)
                if num & (1 << i):
                    count += 1
            if count % 3 != 0:
                ans += "1"
            else:
                ans += "0"
        val = int(ans[::-1], 2)
     
        if neg % 3 != 0:
            return 0 - val
        return val