# 這題是要找第 n 個 ugly number 是多少(ugly number N = 2^p * 3^q * 5^k，只有235為因數的數字)
# 做法就是先在 class 裡面直接做出一個 ugly number list，然後再找第幾個的時候就可以直接找 index 回傳就可以了
# 最一開始的時候有傻傻地放在函數裡面，每次都要重新建 list 會很花時間，所以要改成在外面先建再去找值就好了

class Solution:
    ls = sorted([2**a * 3**b * 5**c for a in range(32) for b in range(20) for c in range(14)])
    def nthUglyNumber(self, n: int) -> int:
        return self.ls[n-1]
