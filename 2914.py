# ===== Question =====
# 給定一個長度為偶數的二進位字串 s，可以透過將 0 改成 1 或 1 改成 0 進行修改。
# 目標是讓字串能夠被分割成一個或多個長度為偶數的連續子字串，且每個子字串內的字元都相同(全 0 或全 1)
# 請計算達成上述條件所需要的最少字元修改次數。

# ===== Thoughts =====
# 這題有要求都是要"偶數"的字串或子字串，所以可以把 0 跟 1 做分群
# 群組奇數個時就從後面拉一個轉換湊成偶數長度，並且計算一次使用，一直做到結束就可以了
# 如果把分群的概念作更延伸的考量時，結合偶數的特性，知道說 2n 跟 2n + 1 這樣一組是最基本的組合
# 所以可以確認這些最基本的組合確認看看需要變換幾次，基本組合不一致就是換一次
# 這樣就可以只走一遍就可以算出結果了

# Method 1 - Groupby
class Solution:
    def minChanges(self, s: str) -> int:
        gp = groupby(s)

        prev = 0
        count = 0

        for key, group in gp:
            c = len(list(group))
            if prev & 1:
                c -= 1
                count += 1    
            prev = (c & 1)
        
        return count

# Method 2 - Neighbor comparison
class Solution:
    def minChanges(self, s: str) -> int:
        return sum([1 for idx in range(0, len(s), 2) if s[idx] != s[idx + 1]])
