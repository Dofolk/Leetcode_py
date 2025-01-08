# 這題是給一個字串的 list，然後在 i < j 的條件下，確認對於第 i 個位置的字串是不是第 j 個位置的開頭跟結尾，如果是就計數，算總共有幾對
# 因為限制條件比較小，所以直接暴力解就可以了，使用 python string 內建的 startswith 跟 endswith 來做判斷
# 是就計數 + 1，全部跑一遍之後回傳就可以了

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        L = len(words)
        for idx in range(L):
            for comp in range(idx + 1, L):
                if words[comp].startswith(words[idx]) and words[comp].endswith(words[idx]):
                    count += 1
        return count
