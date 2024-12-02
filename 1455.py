# 這題是給一串文字，然後給關鍵字，去找看看這關鍵字是不是這串文字裡的單字字首，是的話回傳第幾個單字，不是就回傳-1
# 先用 split() 來分好單字，接著遍尋一遍就好

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        L = len(searchWord)
        words = sentence.split(" ")
        for idx in range(len(words)):
            if len(words[idx]) >= L and words[idx][:L] == searchWord:
                return idx + 1
        return -1
