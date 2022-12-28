class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        a = {}
        b = {}
        for m in matches:
            w = m[0]
            l = m[1]
            if w in a:
                a[w] += 1
            else:
                a[w] = 1
            if l in b:
                b[l] += 1
            else:
                b[l] = 1
        ans1 = []
        ans2 = []
        for w in a:
            if w not in b:
                ans1.append(w)
        ans1.sort()
        for l in b:
            if b[l] == 1:
                ans2.append(l)
        ans2.sort()
        return [ans1, ans2]
        