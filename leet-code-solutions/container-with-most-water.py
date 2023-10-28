class Solution:
    def maxArea(self, height: List[int]) -> int:
        print("workig")
        large = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            if height[left] < height[right]:
                
                large = max(large, height[left] * (right - left))
                left += 1
            else:
                large = max(large, height[right] * (right - left))
                right -= 1
        return large
            
        