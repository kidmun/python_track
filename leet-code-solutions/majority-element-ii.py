class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        person1, person2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == person1:
                count1 += 1
            elif num == person2:
                count2 += 1
            elif count1 == 0:
                person1 = num
                count1 += 1
            elif count2 == 0:
                person2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0

        for num in nums:
            if person1 == num:
                count1 += 1
            if person2 == num:
                count2 += 1
        n = len(nums)
        ans = []
        if count1 > n // 3:
            ans.append(person1)
        if count2 > n // 3:
            ans.append(person2)

        return ans

        
        