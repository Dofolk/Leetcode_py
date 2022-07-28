class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        
        for i in range(len(s)):
            v = ord(s[i])
            if (v>=65 and v<=90):
                ls.append(v+32)
            elif(v>=97 and v<=122):
                ls.append(v)
            elif(v>=48 and v<=57):
                ls.append(v)
        
        length = len(ls)
        if length<=1:
            return True
        
        for i in range(length//2):
            if ls[i]!=ls[length-i-1]:
                return False
        return True
      
# 看有沒有對稱
# 最簡單的做法，把字串走一遍，然後用ascii來將遇到的大些英文變小寫，順便儲存英文及"數字"的ascii
# 最後的判斷之前友遇過了，砍半，頭尾比對，收工！
# 重點是，數字有算進比對的字符
# 數字有算進比對的字符
# 數字有算進比對的字符
# 數字有算進比對的字符
# 哭阿，數字
