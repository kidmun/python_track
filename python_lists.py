if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        com = input().split()
        if com[0] == "insert":
            li.insert(int(com[1]), int(com[2]))
        elif com[0] == "print":
            print(li)
        elif com[0] == "remove":
            li.remove(int(com[1]))
        elif com[0] == "append":
            li.append(int(com[1]))
        elif com[0] == "sort":
            li.sort()
        elif com[0] == "pop":
            li.pop()
        elif com[0] == "reverse":
            li.reverse()
        