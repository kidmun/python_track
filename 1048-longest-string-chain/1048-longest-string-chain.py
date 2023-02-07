class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda item: (-len(item), item))
        count = {}
        for word in words:
            if len(word) in count:
                count[len(word)].append(word)
            else:
                count[len(word)] = [word]
                                                   
        ans = 1
        index = 0
        total = 0
        prev = None
        ans = 1
        for key, word in count.items():
            for i in range(len(word)):
                if (len(word[i]) + 1) not in count:
                    count[key][i] = (word[i], 1)
                    
                 
                else:
                    n = len(count[len(word[i]) + 1])
                    c = 0
                   
                    larg = 1
                  
                    while c < n:
                        w = count[len(word[i]) + 1][c][0]
                        if (len(word[i]) + 1) == (len(w)):
                            flag = False
                           
                            for ind, el in enumerate(w):
                                p = list(w)
                                k = p.pop(ind)
                                if p == list(word[i]):
                                    flag = True
                                    break
                                             
                            if flag:
                                
                                larg = max(larg, count[len(word[i]) + 1][c][1] + 1)
                                ans = max(ans, larg)
                        c += 1
                    count[key][i] = (count[key][i], larg)
      
        return ans

                
                
                        

                
                
                
           

                        

                    
                    
        
                
        
       
        
        
        