class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ma = []
        ran = int(math.log(max(nums), 2)) + 1
        for i in range(ran):
            flag = False
            for num in nums:
                if num & (1<<i):
                    flag = True
                    break
            if flag:
                ma.append("1")
            else:
                ma.append("0")
        ma.reverse()
        ma = int("".join(ma), 2)
        ans = 0
        def backtrack(start, track):
            nonlocal ans
            if track:
                cur = track[0]
                for i in range(1, len(track)):
                    cur |= track[i]
                if ma == cur:
                    ans += 1
            if start >= len(nums):
                return 
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(i + 1, track)
                track.pop()
        backtrack(0, [])
        return ans