class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        def visited(track, k):
            return (track & (1<<k)) != 0
        def off(track,k):
            return track & ~(1<<k)
        def on(track, k):
            return track | (1<<k)
        count = 0
        def backtrack(track, path):
            nonlocal ans, count
            count += 1
            flag = False

            if path and (path[-1] % (len(path)) != 0 and (len(path)) % path[-1] != 0):
                flag = True
                return  
            if len(path) >= n:
                ans += 1
                return
    
            for i in range(1, n+1):
                if visited(track,i): 
                    continue
                path.append(i)
                track = on(track, i)
                backtrack(track, path)
                path.pop()
                track = off(track, i)
        backtrack(0,[])
        return ans