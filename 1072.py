# 這題是給一個 2d array，然後現在能任意選擇選擇 column來將其所有數字做 1 0 之間的轉換，問：最多可以有幾條 row 是同樣的數值
# 這題的想法是當 row X 跟某個 K 做 XOR 是 X^K = all0 or ALL1，這時候再做一次 K 的 XOR 會變成 X = X^K^K = (ALL0 or ALL1) ^ K
# 這邊就可以得到 X 的分解式了，所以可以透過全 1 的 K 來將 X 找出來，而從 X^K = all0 or ALL1 也可以知道說我把 K 做 ALL0 or ALL1 的 XOR 的話就會變成 X
# 所以這邊就可以先分成開頭的數字，可以是 0 也可以是 1，然後對於另一種開頭的舊作 ALL1 XOR，去找出哪些會是可以湊再一起的
# 最後用 counter 來算數目就好



class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freq = Counter()
        
        for row in matrix:
            # 選擇開頭是 0，並且將開頭是 1 的做 ALL1 XOR 來轉成0開頭看看是不是同一個類的
            pattern = tuple(row) if row[0] == 0 else tuple(element^1 for element in row)
            freq[pattern] += 1
        
        return max(freq.values())
