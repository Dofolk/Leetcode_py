# 這題是給一個長度為 L 的大寫字母的字串，然後要看看長度從 1 到 L 的字母排列組合有幾組
# 這題可以用數學的排列組合加上 backtrack 來做，backtrack 負責找出每個字母在長度 n 的組合(curr)中有幾種排列方法
# 確認完 curr 的組合後，就用 backtrack 去找下一個要處理的組合，一直到所有組合都被 backtrack 過
# 所以這邊 backtrack 的做法就是用 for 迴圈來一個一個把字母加進去要處理的組合裡，等後面的字母組合都做完之後，就換掉(DFS 的想法)
# 最後回傳最終結果前要記得 -1，這個 -1 的意思就是說當組合內沒有任何字母時多計算到的一次

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        remain = list(collections.Counter(tiles).values())
        ans = 0
        curr = [0 for _ in range(len(remain))]

        def bt(idx):
            nonlocal ans
            permutation = 1
            for x in curr:
                permutation *= math.factorial(x)
            ans += math.factorial(sum(curr)) // permutation

            for i in range(idx, len(remain)):
                if remain[i] > 0:
                    curr[i] += 1
                    remain[i] -= 1
                    bt(i)
                    curr[i] -= 1
                    remain[i] += 1
        
        bt(0)
        return ans - 1
