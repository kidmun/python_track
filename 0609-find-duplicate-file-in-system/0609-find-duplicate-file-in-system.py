class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        n_paths = []
        for p in paths:
            n_paths.append(p.split())
        obj = {}
        for p in n_paths:
            for i in range(1, len(p)):
                f_name = ""
                j = 0
                while p[i][j] != '(':
                    f_name += p[i][j]
                    j += 1
                val = ""
                j += 1
                while j < (len(p[i]) - 1):
                    val += p[i][j]
                    j += 1
                    
                    
                key = p[0] + "/" + f_name
            
                obj[key] = val
        counter = {}
        for key, amount in obj.items():
            if amount in counter:
                counter[amount] += 1
            else:
                counter[amount] = 1
        ans = []
        for content in counter:
            
            if counter[content] > 1:
                
                dup = []
                for key, amount in obj.items():                    
                    if content == amount:
                        dup.append(key)
                if len(dup) > 0:
                    ans.append(dup)
        return ans
         
                        
                        
            
            
       