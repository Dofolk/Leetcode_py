# 這題是要找第一個不重複的字元的 index ，如果都是重複的話就回報-1
# 第一種做法就是用一個 list 存遇到過且數量大於1的字元，直接用 string.count() 就可以了
# 第二種方法就是用內建的 collections 模組做計數，最後再看看有沒有就好了，這邊的模組還是要 import

class Solution:
  
# Solution 1
    def firstUniqChar(self, s: str) -> int:
        d = []
        for i in range(len(s)):
            if s[i] in d:
                continue
            elif s.count(s[i]) > 1:
                d.append(s[i])
            else:
                return i
        return -1
      
# Solution 2
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
