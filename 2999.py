# === Description ===
# 題目是給一個起始數值 start, 結束數值 finish，位數數值限制 limit 以及必要的後綴數值字串 s
# 問 [start, finish] 之間，擁有後綴是 s，並且後綴外的每個位數數值都 < limit，這樣的數值有幾個
# ex: [1, 6000], limit = 3, s = "123"，answer = 4，有 123, 1123, 2123, 3123，4123的 4 > 3 所以不合條件
# === Thought ===
# 這題可以想說，固定後綴的狀態下，[start, finish] 的數值個數其實就是 [0, finish] - [0, start]
# 所以可以用一個額外的計算函式 calculate 來算看看 [0, finish/start] 符合後綴條件的數值個數
# 在 calculate(x, limit, s)，x 是輸入的字串， limit 跟 s 就是題目原本的
# 首先判斷字串長度，x 的長度比 s 的長度短代表不可能會有符合條件的數值落在 [0, x]之間
# 如果長度相同就確認領頭數字有沒有比較大，比較大代表可以拿到一個完整的 s，不然一樣是 0 (ex: s = "123", x1 = "111", x2 = "200")
# 長度確認完之後就看看總共能拿到多少東西，count 來記錄能拿多少東西，prefix_len 來看 x 跟 s 相差的位數有幾位，代表有多少位數的東西可以做數量累積
# 接著對 x 開頭往後逐個位數去找：每個位數能提供多少種可能，所以要判斷每個位數的數字還有 limit 誰比較大
# 如果 limit 比當下位數(idx)還小的話就代表說到 idx 可以提供多餘限制的數值數量，這時候就把 limit + 1 (讓 idx 包含數字 0 的組合的意思)後去算後面能提供的有多少個
# 這代表說給的位數可以超量供給，所以直接算總數就可以了
# 如果提供的數值比較少，就依照 idx 的數值去計算就好，然後就進入下一個位數的數量累積
# 這邊的想法就是 idx 能提供 1 ~ idx_num 的選擇，然後進入下一輪就代表說讓 idx 是 0
# 假設一直到最後都跑完了，每個 idx 都少量供給的話就需要額外多確認前面 idx 全是 0 的狀況有沒有比後綴 s 還大
# 有的話就代表全 0 還可以提供一個 s 出來，就要把 count + 1
# 最後回傳 count 就可以找出 [0, x] 之間符合 '位數數值限制' 以及 '後綴限制' 的數值個數
# === Code ===

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        start, finish = str(start - 1), str(finish)
        return self.calculate(finish, limit, s) - self.calculate(start, limit, s)
    def calculate(self, x, limit, s):
        if len(x) < len(s):
            return 0
        if len(x) == len(s):
            return 1 if x >= s else 0
        
        prefix_len = len(x) - len(s)
        count = 0
        
        for idx in range(prefix_len):
            if limit < int(x[idx]):
                count += (limit + 1) ** (prefix_len - idx)
                return count
            count += int(x[idx]) * (limit + 1) ** (prefix_len - idx - 1)
        if x[prefix_len:] >= s:
            count += 1
        return count
