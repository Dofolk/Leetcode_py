class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in zip(*strs):
            a = "".join(i)
            if len(set(a)) != 1:
                return res
            else:
                res += a[0]
        return res
      
# 找最長的一樣的字元串
# 利用'zip'函數(很好用)，將字串中的字元依序組合起來
# 接著再將結果變成set，檢查長度就可以了
# python可以不用像C語言那樣要慢慢取字串比對
