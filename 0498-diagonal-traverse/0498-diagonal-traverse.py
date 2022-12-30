class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        obj = {}
        for i in range(len(mat)):
            li = []
            for j in range(len(mat[0])):
                if (i + j) in obj:
                    obj[i+j].append(mat[i][j])
                else:
                    obj[i+j] = [mat[i][j]]
        ans = []
        for key, amount in obj.items():
            if key % 2 == 0:
                amount.reverse()
            for a in amount:
                ans.append(a)
        return ans
            
                
        
                
        