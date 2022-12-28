# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
li = input().split()
li = [int(x) for x in li]
t = tuple(li)
print(hash(t))