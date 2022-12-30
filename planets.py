T = int(input())
for i in range(T):
    planet_info = input().split()
    n, c = int(planet_info[0]), int(planet_info[1])
    planets = input().split()
    counter = {}
    for p in planets:
        if p in counter:
            counter[p] += 1
        else:
            counter[p] = 1
    cost = 0
    for p, freq  in counter.items():
        if freq > c:
            cost += c
        else:
            cost += freq
    print(cost)