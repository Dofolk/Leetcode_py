class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        table = [1]
        s = 1
        for i in range(rowIndex):
            s *= (i+1)
            table.append(s)
        
        ls = []
        for i in range(rowIndex+1):
            ls.append(int(table[rowIndex]/(table[i]*table[rowIndex-i])))
        
        return ls
      
# 做出排列組合的C的表
# 然後用二項分布逐項列出就可以了
