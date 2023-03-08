# 這題會給一個英文大寫字母字串還有一個數字 k，在可以更改 k 個字母德狀況下，最長可以拿到多長的連續相同字母字串
# 這題的做法就是去找每個字母拿到多長，所以就是把字串跑一遍，然後遇到字母之後把長度加上去，當超過可修改的大小時就把長度以前的東西修改掉

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen, largest = 0, 0
        arr = collections.Counter()
        for idx in range(len(s)):
            arr[s[idx]] += 1
            largest = max(largest, arr[s[idx]])
            if maxlen - largest >= k:
                arr[s[idx - maxlen]] -= 1
            else:
                maxlen +=1
        return maxlen
