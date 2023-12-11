class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            ans["".join(sorted(word))].append(word)
        return ans.values()
            
            

