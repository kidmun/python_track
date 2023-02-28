class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        prev = set()
    
        for ch in s:
            
            if ch not in prev:
                    while stack and ch < stack[-1] and count[stack[-1]] > 0:
                        prev.remove(stack[-1])
                        stack.pop()
                    stack.append(ch)
                    prev.add(ch)
                    count[ch] -= 1

            else:
                count[ch] -= 1
      
        return "".join(stack)
                
                

        