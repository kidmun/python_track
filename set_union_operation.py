# Enter your code here. Read input from STDIN. Print output to STDOUT

n_eng = int(input())
eng = set(input().split())
n_fren = int(input())
fren = set(input().split())

print(len(eng.union(fren)))