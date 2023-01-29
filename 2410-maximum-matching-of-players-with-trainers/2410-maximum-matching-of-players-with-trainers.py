class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        p1 = 0
        p2 = 0
        
        while p1 < len(players) and p2 < len(trainers):
            if players[p1] <= trainers[p2]:
                p1 += 1
                p2 += 1
                res += 1
            else:
                p2 += 1
        return res
        