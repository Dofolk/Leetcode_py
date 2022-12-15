# 這題是要找給定區間的左右端點，在這個閉區間內， bitwise AND 的值多少
# 想法就是先把數字變成二進位，如果回傳值是大於 0 的話，就代表說左右端點的二進位前面有一部份相同
# 所以就是用 bit 右移跟 while 來完成(一直找到兩數字相同的時候)，最後再把移除掉的位數給補回來(用左移)
# 如果數字不在同一個等級(二進制領導位數不同，ex: 2^2 跟 2^4)
# 那小的數字在進位的時候就會讓後面的所有值變成 0，再加上最一開始的大小差距讓前面的位數也變成 0，這樣結果就會是 0，也可以用上面的方法做到

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return right << i
