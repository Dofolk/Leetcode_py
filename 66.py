class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = len(digits)
        v = 1
        L = []
        for i in range(d):
            v += digits[i]*pow(10,d-i-1)
        s = str(v)
        for i in range(len(s)):
            L.append(int(s[i]))
        return L
      
# 將數字+1
# 這方法是用型別轉換來完成的
# 另一個方法就是直接操作
# 因為遇到9會進位，所以先來判斷有沒有9，有的話就清0<沒有的話就直接+1
# 因為要不是第一位遇到就直接+1給他，要不就進位再+1值到沒有遇到9
# 最後的return補一個1在最前面，因為真的會跑出去的狀況就是全部都9
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n):
            idx = n-i-1
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        return [1]+digits
'''
