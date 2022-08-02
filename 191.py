class Solution:
    def hammingWeight(self, n: int) -> int:
        s = format(n,'b')
        num = 0
        for i in range(len(s)):
            if s[i]=='1':
                num += 1
        return num
      
# 這題要算二進制表示中有多少個數字 1
# 先用 format 將庶子轉成二進制，這邊不用bin()的原因是可以少跑最前面的 0b
# 然後就用 for loop 逐個計算就收工了
