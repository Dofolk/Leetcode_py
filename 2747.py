# ===== Question =====
# 給定 n 台伺服器，以及記錄各台伺服器收到請求時間的 logs。
# 對每個查詢時間 q，計算在區間 [q - x, q]（包含兩端）內完全沒有收到請求的伺服器數量。
# 依照 queries 的原始順序回傳結果。

''' Thoughts
依照時間序來確認每個 query interval 有幾台 server 是曾經忙碌過的
並且將 logs 也依照時間序來排列，好算出每個 query interval 之間從左而右需要被計算的 logs 有哪些
counts: 記錄一個 query interval [q - x, q] 之間有每一台 server 誰有運作過
left, right: [left, right] 被包含在 [q - x, q] 裡面需要被計算的 log 左邊界跟又邊界

就算有重複打 server 的也沒關係，在 logs 的 sliding window 的右邊界時會重複計算，但不會真的加上去，因為這邊只記錄 0 -> 1 的過程；在左邊界推到重複值的時候遇到重複值也會只計算 1 -> 0 的過程。
'''

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda log: log[1]) # 用時間先後來排序 logs
        counts = [0] * (n + 1)
        active = left = right = 0 # 初始化資訊
        ans = [0] * len(queries)

        # 依照每個 query 時間 q 去算 query interval [q - x, q] 之間要包含的 logs[left] ~ logs[right] 是哪些，並計算啟動過的 server 數量
        for idx, q in sorted(enumerate(queries), key = lambda query: query[1]):
            # 定位出 logs 裡面時間戳記 <= q 的邊界在哪 
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                active += not counts[server]
                counts[server] += 1
                right += 1
            
            # 定位出 logs 裡面時間戳記 < q - x 的邊界在哪，要移除掉不能計算到
            window_left = q - x
            while left < right and logs[left][1] < window_left:
                server = logs[left][0]
                counts[server] -= 1
                active -= not counts[server]
                left += 1
            
            ans[idx] = n - active
        
        return ans
