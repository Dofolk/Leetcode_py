class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        
        for m,n in zip(s,t):
            if m not in s_t and n not in t_s:
                s_t[m] = n
                t_s[n] = m
            elif s_t.get(m)!=n or t_s.get(n)!=m:
                return False
        
        return True
                
# 這題要看看兩個字串的結構有沒有一樣
# 想法建立在 "一樣的概念=文字的1-1 map"
# 所以遇字就存當下的對應值進字典，遇到重複值就從字典拉出來比對有沒有一樣
