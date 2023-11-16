class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = Counter()
        played= Counter()
        all = set([])
        for a, b in matches:
            count[b] += 1
            played[a] += 1
            all.add(a)
            all.add(b)
        ans1 = []
        ans2 = []
        for pl in all:
            if count[pl] == 0 and played[pl] > 0:
                ans1.append(pl)
            elif count[pl] == 1:
                ans2.append(pl)
        ans1.sort()
        ans2.sort()
        return [ans1, ans2]
            
            
        
        