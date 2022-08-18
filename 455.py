# 這題是要把餅乾分給小朋友，能分給越多人越好
# 首先先判斷有沒有餅乾，然後就將小朋友的飢餓度及餅乾的飽足度做倒序排序
# 最後在逐個確認餅乾能不能滿足最不飢餓的小朋友，滿足了就 pop() ，等都完成之後就看跟原始的長度差在哪邊就知道滿足幾個小朋友了

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s_len = len(s)
        if s_len == 0: return 0
        g.sort(reverse = True)
        s.sort(reverse = True)
        g_len = len(g)
        
        for i in range(s_len-1,-1,-1):
            if not g:
                return g_len
            if s[i] >= g[-1]:
                g.pop()
        
        return g_len-len(g)
