# 這題是要把字串的數字變成整數，然後遇到的第一個字元(除了空白)如果不是 "+,-" 或 0~9 的話就直接當成0，其餘的狀況直接0
# 按照規則走，先把塊白給去除，然後抓看看有沒有遇到正負號，最後就開始檢測接著的數字是多少，用 while 來判斷有沒有 digit，有就坐加總，沒有就直接跳出 while 並回傳結果

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1 
        result = 0
        index = 0
        n = len(s)
        
        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)
        
        while index < n and s[index] == ' ':
            index += 1
        
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1
        
        while index < n and s[index].isdigit():
            digit = int(s[index])
            
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                
                return INT_MAX if sign == 1 else INT_MIN
            
            result = 10 * result + digit
            index += 1
        
        return sign * result
