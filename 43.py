# 這題是給兩個數字字串，然後回傳相乘之後的數字字串，題目說操作時不要直接轉換文字
# 作法好幾種，就是把字串變成數字，只是沒有直接用int()，逐位數變成數字就可以了

class Solution:

# 1(沒有用字典)
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 += (ord(num1[i])-ord('0'))*pow(10,len(num1)-i-1)
        for i in range(len(num2)):
            n2 += (ord(num2[i])-ord('0'))*pow(10,len(num2)-i-1)
        return str(n1*n2)
# 2(用字典找數字)
    def multiply(self, num1: str, num2: str) -> str:
        D = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 += D[num1[i]]*pow(10,len(num1)-i-1)
        for i in range(len(num2)):
            n2 += D[num2[i]]*pow(10,len(num2)-i-1)
        return str(n1*n2)
        
