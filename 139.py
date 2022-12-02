# 這題是給一個字串跟單字字典(單字都是唯一的)，然後去看看字串能不能用字典的字做出字串分割(字典的字可以重複使用，但字串內的不行)
# 想法就是在字串中逐個去看可能性，取找看看說現在走到的這個 index 往前去找能不能把字典的字找一個塞進去是符合的
  # 可以找到的話就把當下 index 改成 True，來代表說我可以在這邊切割出個單字來
  # 不行的話就往下一個單字去找
# 找的時候還是要去看看說我所在的 index_now 往前一個字母的長度那一個上次的 index_before(=index_now - lenOfword) 有沒有做出單字的切割
  # 前面沒有做出來的話代表說你這個單字不能用，因為前面已經踩空了，就不可能會有後面單字的切割出現
  # 前面如果有做出來的話就代表說，前面已經有一個切個是合法的，那我就是延續這個合法切割再往下切現在要檢查的這個單字有沒有也合法

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        L = len(s)
        dp = [False]*(L)
        for i in range(L):
            for word in wordDict:
                wL = len(word)
                if i >= wL-1 and (i==wL -1 or dp[i-wL]):
                    if s[i-wL+1:i+1]==word:
                        dp[i] = True
                        break
        return dp[-1]
