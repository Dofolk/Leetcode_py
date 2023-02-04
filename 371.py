# 這題是要做兩個數字的相加，題目是有要求不要用 + -
# 做法就是用位原來計算，先設定一個 mask 來過濾數字，把 a 當成最後要回傳的東西，把 b 當成是要進位的內容
# 先看看要進位的內容有啥(b&mask)，然後去看看說那些地方要進位就直接給他進位(a&b<<1)
# 然後 a 先留好沒進位的部分(當成是手上拿好的數字)，然後讓要進位的部分變成 b 進到下一輪再去做計算

class Solution:
  def getSum(self, a: int, b: int) -> int:
    return a+b


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        
        while (b & mask) > 0:
            carry = ( a & b ) << 1
            a = (a ^ b)
            b = carry
        
        return (a & mask) if b > 0 else a
