class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        queue = deque([0])
        visited = set([0])
        while queue:
            n = len(queue)
            for i in range(n):
                room = queue.popleft()
                for num in rooms[room]:
                    if num not in visited:
                        queue.append(num)
                        visited.add(num)
        if len(rooms) == len(visited):
            return True
        return False