class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
#         large = arr[-1]
        
#         prev = large
#         for i in range(len(arr) - 2, -1, -1):
#             large = max(large, prev)
#             prev = arr[i]
#             arr[i] = large
#         arr[-1] = -1
#         return arr
        
        ans = [-1]
        large = arr[-1]
        for i in range(len(arr) - 1, 0, -1):
            large = max(large, arr[i])
            ans.append(large)
        ans.reverse()
        return ans
            
        