# Enter your code here. Read input from STDIN. Print output to STDOUT

k = input()
room_number = input()
c = {}
li = room_number.split()

for room in li:
    if room in c:
        c[room] += 1
    else:
        c[room] = 1
        

for room in c:
    if c[room] == 1:
        print(room)
