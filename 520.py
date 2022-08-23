# 這題要判斷給的字串是不是全部大寫或全部小寫或是首字大寫
# 做法就是用內建函式們來解決

class Solution:
  
# Solution 1
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
      
# Solution 2
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower(): return True
        if word[1::].islower(): return True
        return False
