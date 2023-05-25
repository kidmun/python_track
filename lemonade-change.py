class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = Counter()
        for bill in bills:
            if bill == 20:
                if count[5] == 0 or (count[10] < 1 and count[5] < 3):
                    return False
                elif count[10] > 0:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] > 2:
                    count[5] -= 3
                count[20] += 1 
            elif bill == 10:
                if count[5] < 1:
                    return False
                count[5] -= 1
                count[10] += 1
            else:
                count[5] += 1
        return True