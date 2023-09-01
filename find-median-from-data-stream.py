from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or -self.left[0] >= num:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)
        if (len(self.left) - len(self.right)) > 1:
            val = heappop(self.left)  
            heappush(self.right, -val)
        elif (len(self.right) - len(self.left)) > 1:
            val = heappop(self.right)  
            heappush(self.left, -val)


    def findMedian(self) -> float:
       
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        if len(self.left) > len(self.right):
            return -self.left[0] 
        return self.right[0]
        
        
       
  

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()