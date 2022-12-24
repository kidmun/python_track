# Enter your code here. Read input from STDIN. Print output to STDOUT

first_line = input()
happ = 0
arr = input().split()
A = set(input().split())
B = set(input().split())

for num in arr:
    if num in A:       
        happ += 1
    if num in B:         
        happ -= 1
print(happ)
