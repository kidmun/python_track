class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        ans = 0
     
        def dp(p, cur, fu):
            nonlocal ans
            if fu > fuel:
                return False
            if cur == finish:
                ans += 1
            for i in range(len(locations)):
                if i != cur:
                    p.append(i)
                    val = dp(p, i, fu + (abs(locations[i] - locations[cur])))
                    p.pop()
        dp([start],start, 0)
        print(ans)



        return ans % (10**9 + 7)