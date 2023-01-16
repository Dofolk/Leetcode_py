# 這題是會給一個字串的list，然後找出其中兩個字母不重複的字船，長度相乘最大是多少
# 做法就是用 bit 操作來處理，先宣告一個空間來存每個字有哪些字母，用 bit 的方式來記錄，紀錄方式就是用字母的 ord 來看偏移量就可以了
# 然後再用一個 for loop 來看看有沒有重複(&)並且記錄更新的數字

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask, ans = [0]*len(words), 0
        for i, word in enumerate(words):
            for s in word:
                mask[i] |= 1<< (ord(s)-ord('a'))
            for j in range(i):
                if not mask[i] & mask[j]:
                    ans = max(ans, len(words[i])*len(words[j]) )
        return ans
