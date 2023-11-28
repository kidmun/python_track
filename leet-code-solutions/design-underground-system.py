class UndergroundSystem:

    def __init__(self):
        self.person = {}
        self.count = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.person[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        val = (self.person[id][0],stationName)
        if val not in self.count:
            self.count[val] = (t - self.person[id][1], 1)
        else:
            self.count[val] = (t - self.person[id][1] + self.count[val][0], 1 + self.count[val][1] )
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # print(self.count)
        return self.count[(startStation,endStation)][0]/ self.count[(startStation,endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)