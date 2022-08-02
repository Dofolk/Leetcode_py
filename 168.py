class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s = ''
        while columnNumber:
            s += table[(columnNumber-1)%26]
            columnNumber = (columnNumber-1)//26
        
        return s[::-1]
      
# 把數字變成A~Z表示，這邊要注意的就是序號問題(index)
# 一般我們常用的序號是從1開始，但是在python裡面是0，所以這部分要調整一下
