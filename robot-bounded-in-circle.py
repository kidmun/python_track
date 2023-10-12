class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        ans = [0, 0]
        turn_left = {'n':'w', 'w':'s', 's':'e', 'e':'n'}
        turn_right = {'n':'e', 'w':'n', 's':'w', 'e':'s'}
        prev = "n"
        for i in range(4):
            for j in range(len(instructions)):
                if instructions[j] == "L":
                    prev = turn_left[prev]
                elif instructions[j] == "G":
                    if prev == "n":
                        ans[1] += 1
                    elif prev == "w":
                        ans[0] -= 1
                    elif prev == "s":
                        ans[1] -= 1
                    else:
                        ans[0] += 1
                else:
                    prev = turn_right[prev]
  
        return  ans == [0, 0]