# 這題是要看給的單字有沒有在間盤上同一個 row 
# 第一個做法就是用 set 來看看有沒有符合，先把給的字變成小寫的 set，記錄每個字母在哪個 row，最後看看紀錄的 set 長度是不是1
# 第二個就是用內建函數 issubset()，

class Solution:
  
# Solution 1
    def findWords(self, words: List[str]) -> List[str]:
        row1, row2, row3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        ans = []
        for n in range(len(words)):
            ls = list()
            s = set(words[n].lower())
            for i in s:
                if i in row1: ls.append(1)
                elif i in row2: ls.append(2)
                elif i in row3: ls.append(3)
            if len(set(ls)) == 1:
                ans.append(words[n])
        
        return ans
      
# Solution 2
    def findWords(self, words: List[str]) -> List[str]:
        row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        return [x for x in words if set(x.lower()).issubset(row1) or set(x.lower()).issubset(row2) or set(x.lower()).issubset(row3)]
