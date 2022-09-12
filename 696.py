# 這題是要從字串找出子01數量相同的子字串的數目有幾個
# 做法就是先做分群，因為數量要一樣，所以分群之後可以看到 01 分別的分群數量有多少後直接湊起來找最小的那個數字
# 又因為是要01連續在一起才能算子字串的數目，所以湊起來的0或1的數量就會是這樣湊起來組合所能產生的最多子字串數目
# for ex, 0001111有三種，01 0011 000111，不會有其他的東西，因為0要跟0一群，1跟1一群

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group = [1]
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                group.append(1)
            else:
                group[-1] += 1
        ans = 0
        for i in range(1,len(group)):
            ans += min(group[i], group[i-1])
        return ans
