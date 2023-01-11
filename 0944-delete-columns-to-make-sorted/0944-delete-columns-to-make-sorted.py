class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            cur_asc = ord(strs[0][i])
            ordered_flag = True
            for j in range(1, len(strs)):
                if ord(strs[j][i]) < cur_asc:
                    ordered_flag = False
                    break
                else:
                    cur_asc = ord(strs[j][i])
            if not ordered_flag:
                res += 1
                
        return res
                
                
            
        