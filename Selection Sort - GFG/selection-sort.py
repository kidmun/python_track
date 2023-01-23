#User function Template for python3

class Solution: 
    def select(self, arr, i):
        minimum = i
        for j in range(i + 1, len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
        return minimum
        # code here 
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n - 1):
            minimum = self.select(arr, i)
            
            arr[i], arr[minimum] = arr[minimum], arr[i]
            
        return " ".join(map(str, arr))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends