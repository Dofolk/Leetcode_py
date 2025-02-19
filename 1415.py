# 這題是給一個數字 n 跟 k，n 是指字串(只由abc三字母組成)的長度，k 是指長度 n 的字串集下，排序第 k 個的字串是哪個，如果 k 超出字串集的數量之外就回傳空字串
# 這題可以用 bisect 的想法來做，因為每個開頭就是 a b c，騎往下分支就是 3 x 2 x ... x 2，共 n - 1 個 2
# 這樣就可以先把 k 先確定開頭會是 a b c 的哪一個，就把 k 減掉分區的標準，就可以確立開頭是要 abc 哪一個
# 接著就可以對每個位置做出數字的定位，先找出前面那些開頭的狀況下，這邊 k 的中間值在哪裡以及 k 比較偏向小的還是大的
# 然後就可以建立字典來看看偏小的數字，依據前面字母來決定後面這個字母偏小的話該是哪個，反之偏大也是
# 這樣就可以對於中間值來判斷後面的字母要填上偏大還是偏小的就可以了
# 最後就可以回傳總結下來的結果就可以了

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""
        
        res = ["a"] * n
        next_small = {"a" : "b", "b" : "a", "c" : "a"}
        next_great = {"a" : "c", "b" : "c", "c" : "b"}
        start_a = 1
        start_b = start_a + (1 << (n - 1))
        start_c = start_b + (1 << (n - 1))

        if k < start_b:
            res[0] = "a"
            k -= start_a
        elif k < start_c:
            res[0] = "b"
            k -= start_b
        else:
            res[0] = "c"
            k -= start_c
        
        for idx in range(1, n):
            mid = 1 << (n - idx - 1)
            if k < mid:
                res[idx] = next_small[res[idx - 1]]
            else:
                res[idx] = next_great[res[idx - 1]]
                k -= mid
        
        return "".join(res)
