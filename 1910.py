# 這題是給一個字串 s 跟要移除的字串 part，如果 part 存在 s 裡面就移除，一直移除到沒有 part 為止，問最後 s 變成甚麼樣子
# 例子: s = "yababcab", part = "abc"，第一次做就會把 abc拿掉，就得到 s = "yabab"，發現沒有 abc 了就可以回傳 s 了
# 簡單的做法就是用內建的 str.replace() 來操作，把替換次數設為 1 之後再重複做到不能做就可以了

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)
        return s
