from collections import Counter
# import math
# def isPowerOfTwo(num):
#     if math.log(num,2).is_integer():
#         return True
#     else:
#         return False
    
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        
        power = []
        n = 1
        while n <= 2**21:
            power.append(n)
            n *= 2
        
        freq = Counter(deliciousness)
        for key, amount in freq.items():
            if (key + key) in power and amount > 1:
                count += (amount * (amount - 1))//2
            for p in power:
                value = p - key 
                if value in freq and value != key and key > value:
                    count += (amount * freq[value])
            
                    
                    
                    
        return count % (10 **9 + 7)
        


                
        