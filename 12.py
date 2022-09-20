# 這題是要把數字變成羅馬數字
# 作法就是很基本的照著算就可以了，看是要先列出所有的羅馬文數字再計算或是直接暴力全寫都可以

# 1
class Solution:
    def intToRoman(self, num: int) -> str:
        sym = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        ans = str()
        for val, s in sym:
            if num>=val:
                for _ in range(num//val):
                    ans += s
                num %= val
        return ans
      
# 2
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = str()
        while num>0:
            if num>=1000: 
                ans += 'M'
                num -= 1000
            elif num>=500:
                if num>=900: 
                    ans+='CM'
                    num -= 900
                else: 
                    ans+='D'
                    num-=500
            elif num>=100:
                if num>=400: 
                    ans+='CD'
                    num-=400
                else: 
                    ans+='C'
                    num-=100
            elif num>=50:
                if num>=90: 
                    ans+='XC'
                    num-=90
                else: 
                    ans+='L'
                    num-=50
            elif num>=10:
                if num>=40: 
                    ans+='XL'
                    num-=40
                else: 
                    ans+='X'
                    num-=10
            elif num>=5:
                if num>=9: 
                    ans+='IX'
                    num-=9
                else: 
                    ans+='V'
                    num-=5
            else:
                if num>=4:
                    ans+='IV'
                    num-=4
                else:
                    ans+='I'
                    num-=1
        
        return ans
