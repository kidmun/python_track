class Solution:
    def __init__(self):
        self.val = 0
    def recu(self, li):
        if len(li) >= self.val + 1:
            return li
        new = [1]
        i = 0
        j = 1
        while j < len(li):
            new.append(li[i]+li[j])
            i += 1
            j += 1
        new.append(1)
        return self.recu(new)
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 or rowIndex  == 1:
            return [1] * (rowIndex + 1)
        self.val = rowIndex
        return self.recu([1,1])
        
        
        
        