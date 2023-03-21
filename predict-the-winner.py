class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def predict(left, right, turn):
            if left == right:
                if turn:
                    return [nums[left], 0]
                return  [0, nums[left]]
            val1 = predict(left + 1, right, not turn)
            val2 = predict(left, right - 1, not turn)
            if turn:
                val1[0] += nums[left]
                val2[0] += nums[right]
                if val1[0] > val2[0]:
                    return val1
                return val2
            else:
                val1[1] += nums[left]
                val2[1] += nums[right]
                if val1[1] > val2[1]:
                    return val1
                return val2            
        ans = predict(0, len(nums) - 1, True)
        if ans[0] >= ans[1]:
            return True
        return False