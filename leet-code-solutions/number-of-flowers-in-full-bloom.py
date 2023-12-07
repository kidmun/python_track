class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        line = Counter()
        for a, b in flowers:
          line[a] += 1
          line[b + 1] -= 1
            
        keys = line.keys()
        keys = set(keys)
        for num in persons:
          keys.add(num)
        keys = list(keys)
        keys.sort()
        cur = 0
        for key in keys:
          cur = line[key] + cur
          line[key] = cur
        ans = []
        for num in persons:
          ans.append(line[num])
        return ans

        



        return []
        
        