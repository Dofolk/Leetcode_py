# 這題就是把數列做處理
# 遇到數字可以同時被3,5整除的就改寫成 FizzBuzz，只有5就改寫成 Buzz，只有3就改寫成 Fizz，剩下數字就變成字元留著就好了

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1,n+1,1):
            if not i%15:
                l.append("FizzBuzz")
            elif not i%5:
                l.append("Buzz")
            elif not i%3:
                l.append("Fizz")
            else:
                l.append(str(i))
        return l
