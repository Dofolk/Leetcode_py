class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        nl = len(needle)
        while i<len(haystack)+1:
            if i > len(haystack)-nl:
                i = -1
                break
            if haystack[i] == needle[0]:
                if haystack[i:i+nl] == needle:
                    return i
            i += 1
            
        if i >= len(haystack):
            i = -1
        
        return i
      
# 用python做C的strstr()
# 用while來逐個字元做檢測
# 注意的是如果needle是一個字元的話那就要透過最後一個if來清掉，所以在while的時候偷偷多做一次確定說真的已經超出去了
