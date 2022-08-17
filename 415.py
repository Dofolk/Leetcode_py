# 這題是要算數字字串的相加，但是不能直接用 int() 變換後相加
# 第一種作法就是暴力解，硬是找出數字的 int 型別，相加再變回字元
# 第二種做法就是逐個做計算，用 ord() 來計算，逐個位元做加法

class Solution:
  
# Solution 1
    def addStrings(self, num1: str, num2: str) -> str:
        d = "0123456789"
        v1, v2 = 0, 0
        for i in range(len(num1)):
            v1 += d.index(num1[i])*pow(10,len(num1)-1-i)
        for i in range(len(num2)):
            v2 += d.index(num2[i])*pow(10,len(num2)-1-i)
        return str(v1+v2)
      
# Solution 2
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0": return ''.join(num2[:])
        if num2 == "0": return ''.join(num1[:])
        ans = []
        c = 0
        m = min(len(num1),len(num2))
        L = num1 if len(num1)>len(num2) else num2
        
        for i in range(-1,-m-1,-1):
            add = ord(num1[i]) + ord(num2[i]) - 96 + c
            c = add//10
            ans.append(str(add%10))
        
        for i in range(len(L)-m-1,-1,-1):
            add = ord(L[i]) - 48 + c
            c = add//10
            ans.append(str(add%10))
        
        if c == 1: ans.append("1")
        
        return ''.join(ans[::-1])
