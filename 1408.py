# 這題是給一個唯一字串的 list，然後去確認裡面的字串，回傳哪些是其他字串的子字串
# 做法就是直接暴力解，因為題目的限制很小，所以直接解就可以了
# 第一個做法就是先做長度排序，因為知道唯一，所以最長的不會是答案之一，這種想法出發，從最短的字串開始比跟找
# 當確定是其他字串的子字串時就存起來並且 break，少跑一些後面額外的尋找
# 第二個做法就是用內建函數，先把給定的 list 內的所有字串用空白符號做相連，然後用字串的 .count() 函數來找有出現過幾次
# 直接對 list 裡面的字串都 count 一次就可以回傳了


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        L = len(words)
        if L == 1:
            return ans
        words.sort(key = lambda x: len(x))
        for idx in range(L):
            for j in range(idx + 1, L):
                if words[idx] in words[j]:
                    ans.append(words[idx])
                    break
        return ans

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        string = ' '.join(words)
        return [word for word in words if string.count(word) > 1]
