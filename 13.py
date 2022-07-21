class Solution:
    def romanToInt(self, s: str) -> int:
        D = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        value = 0
        for i in range(len(s)):
            if i == len(s)-1:
                value = value + D[s[i]]
                return value
            if D[s[i]] < D[s[i+1]]:
                value = value - D[s[i]]
            else:
                value = value + D[s[i]]

# 設計邏輯：C在MD前、X在CL前跟I在XV前面會是扣值的，所以變減法就好
# 首先，建立一個字母對數字的dictionary
# 給定一個值為0，開始依據後一位的字母作加減法
# 最後要記得遇到最後一個字元的時候要有個判斷式跳離開
