# 猜數字遊戲，用已經寫好的 guess() 來看目前的數字是高還是低
# 用 binary search 來找數字，依照中間值的大小來調整區間 [a,b] 中要修改哪個值

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 0
        while s<n:
            v = (s+n)//2
            g = guess(v)
            if g == 1:
                s = v + 1
            elif g == -1:
                n = v - 1
            elif g == 0:
                return v
        return s
