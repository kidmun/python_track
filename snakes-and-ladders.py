class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = deque([(1,0)])
        visited = set([1])
        n = len(board)
        while queue:
            length = len(queue)
            print(queue)
            for _ in range(length):
                cur = queue.popleft()
                if cur[0] == n ** 2:
                    return cur[1]
                x = cur[0] + 1
                while x < cur[0] + 7 and x <= n ** 2:
                    val = ceil(x / n)
                    
                    if val % 2 == 0:
                        check = board[n - val][val * n - x]
                    else:
                        check = board[n - val][x - (val - 1) * n   - 1]
                 
                    if x not in visited:
                        visited.add(x)
                        if check != -1:
                            queue.append((check, cur[1] + 1))
                        else:
                            queue.append((x, cur[1] + 1))
                    x += 1      
        return -1