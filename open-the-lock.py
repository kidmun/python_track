class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def rotate(num, add):
            if num == 0 and add == -1:
                return 9
            if num == 9 and add == 1:
                return 0
            return num + add
        queue = deque([[0, 0, 0, 0]])
        deadlocks = set([])
        for d in deadends:
            deadlocks.add(d)
        if "0000" in deadlocks:
            return -1
        deadlocks.add("0000")
        count = 0
        target = [int(x) for x in list(target)]
        while queue:
            length = len(queue)
            for i in range(length):
                current = queue.popleft()
                if current == target:
                    return count
                for i in range(4):
                    val = current[::]
                    val[i] = rotate(val[i], 1)
                    val = [str(x) for x in val]
                    if "".join(val) not in deadlocks:
                        cc = [int(x) for x in val]
                        queue.append(cc)
                        deadlocks.add("".join(val))
                    val = current[::]
                    val[i] = rotate(val[i], -1)
                    val = [str(x) for x in val]
                    if "".join(val) not in deadlocks:
                        cc = [int(x) for x in val]
                        queue.append(cc)
                        deadlocks.add("".join(val))
            count += 1
        return -1