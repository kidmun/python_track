test = int(input())

for t in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    left = 0
    right = 0
    res = 0
    val = float("-inf")
    while right < n:
         
        if (nums[right] >= 0 and nums[left] > 0) or (nums[right] < 0 and nums[left] < 0):
            val = max(val, nums[right])
            right += 1
            
        else:
            
            res += val
            left = right
            val = float("-inf")
    if val:
        res += val
    print(res)