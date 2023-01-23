class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        
        for index in range(n):
            
            largest = max(arr[:n - index])
            largest_index = arr.index(largest) + 1
            arr[:largest_index] = reversed(arr[:largest_index])
            result.append(largest_index)
            arr[:n - index] = reversed(arr[:n - index])
            result.append(n-index)
            
        return result
            
        