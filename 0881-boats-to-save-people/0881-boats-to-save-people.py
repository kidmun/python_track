class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        boats = 0
        right = n - 1
        left = 0
        prev = 0
        while left < right:
            if (people[right] + people[left]) <= limit:
                left += 1
                right -= 1
                        
            else:
                right -= 1
            if left == right:
                boats += 1
            
            boats += 1
            
        return boats
        