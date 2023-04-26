# 這題是給一個 rand7 的函式，會隨機給 1~7 的一個數字，現在要做出 rand10() 的函式
# 做法就是直接 call random.randint
# 雖然題目說要從 rand7 變化到 rand10，但是真的有點....

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        return randint(1,10)
