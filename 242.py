class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        
        s.sort()
        t.sort()
        
        return s==t
      
# 這題要看字串是不是一樣的字串重新排列的結果
# 所以就用 sort 的方式來確認有沒有一樣就可以了
