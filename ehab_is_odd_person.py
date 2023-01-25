n = int(input())
nums = list(map(int, input().split()))
 
odd = []
even = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
        
        
if len(even) == n or len(odd) == n:
    print(*nums)
else:
    print(*sorted(nums))
