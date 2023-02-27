class DataStream:

    def __init__(self, value: int, k: int):
        self.count = 0
        self.queue = []
        self.k = k
        self.value = value
        self.total = 0
        

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.total += 1
        if len(self.queue) < (self.k):
            return False   
        ans = (self.total == self.k)
        if self.queue[self.count] == self.value:
            self.total -= 1
        self.count += 1
        return ans
            
       
            
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)