class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        li = []
        for i in range(1, n + 1):
            li.append(i)
            i = 0
        while len(li) > 1:
            i = i + k - 1
            if i >= len(li):
                i = i % len(li)
            li.pop(i)
            
        return li[0]
            

        
            
        
        
      