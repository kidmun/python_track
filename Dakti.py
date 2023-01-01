n = int(input())
 
 
 
for i in range(n):
    
    words = input().split()
    
    obj = {}
    for word in words:
        
        for w in word:
            if w.isdecimal():
                obj[int(w)] = word.replace(w, "")
                break
    nums = sorted(obj)
    ans = []
    for n in nums:
        ans.append(obj[n])
    print(" ".join(ans))
            
        