class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        
        res = []
        p1 = 0
        p2 = 0
     
        while p1 < n and p2 < m:
           
            
            if word1[p1] > word2[p2]:
                res.append(word1[p1])
                p1 += 1
            elif word1[p1] < word2[p2]:
                res.append(word2[p2])
                p2 += 1
            else:
                if word1[p1:] >= word2[p2:]:
                    res.append(word1[p1])
                    p1 += 1
                else:
                    res.append(word2[p2])
                    p2 += 1

        while p1 < n:
            
            res.append(word1[p1])
            p1 += 1
        while p2 < m:  
           
            res.append(word2[p2])
            p2 += 1
        return "".join(res)

                
            
      
            
        