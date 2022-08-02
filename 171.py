# 這題要把 excel 的英文編號變回數字
# 做法就是從英文字穿的最後往前一個一個做，用ascii code來找數字
# 逐個往前，逐個增加26的次方數


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        v = 0
        length = len(columnTitle)
        for i in range(length-1,-1,-1):
            v += (ord(columnTitle[i])-64)*pow(26,length-i-1)
        return v
