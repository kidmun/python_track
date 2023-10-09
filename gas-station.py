class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pref = []
        for i in range(len(gas)):
            pref.append(gas[i] - cost[i])
        if sum(pref) < 0:
            return -1
        inc = 0
        ind = 0
        for i in range(len(pref)):
            if pref[i] > 0:
                ind = i
                inc = i
                ss = pref[i]
                break
        for i in range(ind + 1, len(gas)):
            ss += pref[i]
            if inc == None and pref[i] > 0:
                inc = i
            elif ss < 0:
                ss = 0
                inc = None  
                if pref[i] > 0:
                    inc = i
                    ss = pref[i]
            
        return inc