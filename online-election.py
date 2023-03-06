class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        count = Counter()
        self.prev = [persons[0]]
        lar = persons[0]
        count[persons[0]] = 1 
        for i in range(1, len(persons)):
            count[persons[i]] += 1
            if count[persons[i]] >= count[lar]:
                lar = persons[i]
            self.prev.append(lar)
        self.n = len(persons)

    def q(self, t: int) -> int:
        left = 0
        right = self.n - 1
        val = bisect_right(self.times, t)
        return self.prev[val - 1]
        

        
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)