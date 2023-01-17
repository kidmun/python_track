class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        obj = {}
        for i in range(len(names)):
            obj[heights[i]] = names[i]
        
#         for i in range(len(heights)):
#             for j in range(len(heights) - 1 - i):
#                 if heights[j] < heights[j + 1]:
#                     heights[j], heights[j + 1] = heights[j + 1], heights[j]
        
#         for i, h in enumerate(heights):
#             names[i] = obj[h]
            
#         return names
        
        # for i in range(len(names) - 1):
        #     large = i
        #     for j in range(i + 1, len(names)):
        #         if heights[j] > heights[large]:
        #             large = j
        #     heights[large], heights[i] = heights[i], heights[large]
        
        for i in range(len(heights) - 1):
            j = i + 1
            cur = heights[j]
            while j > 0 and cur > heights[j-1]:
                heights[j] = heights[j-1]
                j -= 1
            
            heights[j] = cur
                
      
        for i, h in enumerate(heights):
            names[i] = obj[h]
            
        return names
        
        
        