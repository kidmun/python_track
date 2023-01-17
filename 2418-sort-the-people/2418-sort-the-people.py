class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        obj = {}
        for i in range(len(names)):
            obj[heights[i]] = names[i]
        
        for i in range(len(heights)):
            for j in range(len(heights) - 1 - i):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
        
        for i, h in enumerate(heights):
            names[i] = obj[h]
            
        return names
            
        
        
        