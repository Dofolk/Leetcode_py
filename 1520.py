# ===== Question =====
# 題目給一個字串 s，然後要找符合下面條件的不相交子字串數量最多有幾個，然後回傳任意順序即可
# 條件是子字串內有出現的字元 c，那所有 s 裡面的 c 就只能出現在這個子字串內
# 當子字串的選擇有很多的時候，就挑長度最小化的那一些
# for ex1: abccba -> ans = ['cc']，abccba 也符合條件但是它的長度比 cc 還長所以就不要他了
# for ex2: abefbcca -> ans = ['e', 'f', 'cc']

# ===== Thoughts =====
# 主要是 Greedy 的想法，題目的意思可以想成就是找子字串的長度剛好等於所有字元出現次數的總和
# 主要有兩種，一種是單一字元自串，另一種是字元組合字串 -> 先找單一字元再來拚組合
# 所以這裡就可以轉化一下，找區間的話可以透過 find() 跟 rfind() 來找一個字元出現的頭跟尾
# 再透過 collections.Counter() 來算出字元出現的次數
# 接著考慮 ex1 的狀況，可以選擇短的 cc 就不要選擇長的那段，所以遇到一個字元時就先處理他
# 所以這邊用一個 deque() 來記錄自己沒辦法湊出單一字元字串的
# appendleft() 可以優先處理當下字元，來組看看能不能成單一字元，能成的話就清空 deque()
# 清空的目的是我都可以找到被包含在組合字串內長度更短的單一字元字串了，我就不要湊組合字串了，清了！
# 那如果不能組成單一字元字串的話就開始湊組合，用 total 來記錄字元的總出現次數
# 來知道目前字串長度跟總出現次數有沒有一樣，一樣就加到答案內
# 最後回傳答案就好

# Method 1 - Greedy
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        counts = Counter(s)
        first = {c: s.find(c) for c in counts}
        last = {c: s.rfind(c) for c in counts}
        
        res = []
        q = deque()

        for c in counts:
            q.appendleft( (first[c], last[c], counts[c]) )
            
            left = inf
            right = -inf
            total = 0

            for l, r, freq in q:
                total += freq
                if l < left:
                    left = l
                if r > right:
                    right = r
                if total == (right - left + 1):
                    break
            
            if total == (right - left + 1):
                res.append(s[left : right + 1])
                q.clear()
        
        return res
