class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
    
        left = 0
        right = 1
        count = 1
        while right < n:
            if chars[right] == chars[left]:
                
                if right == (n - 1) and chars[right] == chars[left]:
                    
                    if ((right + 1) - left) > 1:
                        val = str((right + 1) - left)
                        for v in val:
                            chars[count] = v
                            count += 1
                right += 1
                    
            else:
                        
                if (right - left) > 1:
                    val = str(right - left)
                    for v in val:
                        chars[count] = v
                        count += 1
                chars[count] = chars[right]
                left = right
                right += 1
                count += 1
        chars = chars[:count]
        return len(chars)