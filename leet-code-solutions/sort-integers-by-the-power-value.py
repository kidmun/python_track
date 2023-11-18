class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power_of_two(num):
            return int(math.log(num, 2)) == ceil(math.log(num, 2))
        def find_power(num, count):
            # print(num, count, "shsh")
            if power_of_two(num):
                return count + int(math.log(num, 2))
            if num % 2 == 0:
                return find_power(num // 2, count + 1)
            return find_power(num * 3 + 1, count + 1)
        ans = []
        for i in range(lo, hi + 1):
            ans.append((find_power(i, 0), i))
        ans.sort()
        # print(ans)
        return ans[k - 1][1]

        # print(find_power(3, 0))
        # return 4

    