class Solution:
    def decodeString(self, s: str) -> str:
        
        def decode(index, n, prev):
      
            if index >= len(s):
                return ""
            elif s[index] == "]":
                prev[0] = index
                return ""
            elif s[index] == "[":
                print(n, n.isnumeric(), prev)
                return int(n) * decode(index+1, "", prev) + decode(prev[0]+1, "", prev)
            elif s[index].isnumeric():
                return decode(index+1, n + s[index], prev)
            else:
                return s[index] + decode(index+1, n, prev)
        prev = [0]
        return decode(0, "", prev)