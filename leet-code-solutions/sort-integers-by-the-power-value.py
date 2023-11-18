class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def power_of_two(num):
            return int(math.log(num, 2)) == ceil(math.log(num, 2))
        def find_power(num):
            if power_of_two(num):
                return int(math.log(num, 2))
            if num in memo:
                return memo[num]
            if num % 2 == 0:
                val = find_power(num // 2)
            else:
                val = find_power(num * 3 + 1)
            memo[num] = val + 1
            return memo[num]
        ans = []
        for i in range(lo, hi + 1):
            ans.append((find_power(i), i))
        ans.sort()
        return ans[k - 1][1]

        

    