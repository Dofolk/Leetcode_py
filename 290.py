# 這題是給一個字元序列跟一串單字序列，看看兩個序列的排列方式有沒有一樣，就是一個字元對一個單字
# 做法就是用字典來搜尋，第一個做法會比較慢，因為有些東西可以用內建函數做就不用自己寫了
# 第二個作法就用到一些內建函數來幫忙做處理，例如 split 跟 zip 來幫忙做

class Solution:
    
# Solution 1    
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = []
        dic1 = dict()
        dic2 = dict()
        p = 0
        for i in range(len(s)):
            if s[i] == " ":
                l.append(s[p:i])
                p = i + 1
            elif i == len(s)-1:
                l.append(s[p:i+1])
                break
        if len(pattern) != len(l):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in dic1:
                dic1[pattern[i]] = l[i]
            if l[i] not in dic2:
                dic2[l[i]] = pattern[i]
            if dic1[pattern[i]] != l[i] or dic2[l[i]] != pattern[i]:
                return False
        
        return True
      
# Solution 2
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split(" ")
        dic1 = dict()
        dic2 = dict()
        
        if len(pattern) != len(l):
            return False
        
        for i,j in zip(pattern, l):
            if i not in dic1:
                if j in dic2:
                    return False
                else:
                    dic1[i] = j
                    dic2[j] = i
            else:
                if dic1[i] != j:
                    return False
        
        return True
