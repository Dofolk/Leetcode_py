# ===== Question =====
# 有 k 台編號為 0 到 k-1 的伺服器，每個請求都有到達時間與處理所需時間。
# 第 i 個請求從 i % k 號伺服器開始，依編號循環尋找第一台空閒的伺服器，若全部忙碌就丟棄請求。
# 回傳處理請求數最多的所有伺服器編號。

# ===== Thoughts =====
# 這題透過 heap 來做，基本想法就是去記錄目前哪些 server 運作中以及那些是閒置的
# 然後根據題目要求的選擇順序去配對當下進來的 task 以及 server

# Method 1 - Directly check
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # 紀錄那些 server 正在運作，紀錄格式(請求處理結束的時間, server 編號)
        busy = []
        # 記錄首選 server 位置後的可用 server 編號
        after = []
        # 記錄首選 server 位置前的可用 server 編號
        before = list(range(k))
        # 紀錄每個 server 跑了幾個任務
        requests_handled = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):

            # 計算首選 server 用哪個
            preferred = i % k

            # 當整個 server 順序輪過一遍並從 index k - 1 要跑回 index 0 server 時重新整理兩個紀錄 list
            # 這邊直接互換就好，因為當跑完一輪從頭時預期後面要是滿的以及前面是空的(因為沒有 index -1)
            if preferred == 0:
                after = before
                before = []

            # 更新雲作中server 列表，如果執行結束時間比目前 task 近來的時間還前面的話
            # 就把 server 給釋放出來，並且依據當下首選決定要把釋放出來的空閒 server 放進 before 還是 after
            # Move all servers that have finished into
            # the appropriate available-server heap.
            while busy and busy[0][0] <= start:
                finish_time, server = heapq.heappop(busy)

                if server >= preferred:
                    heapq.heappush(after, server)
                else:
                    heapq.heappush(before, server)

            # 根據題目需求來選擇要用哪個 server 實際運作現在位置的 task
            # 首選位置之後(after) 如果有可用的 server 時就使用它(題目要求的優先級)
            # 找完之後再去找首選位置之前(before) 看有沒有可用 server
            # 全部可用 server 都找完之後還是沒有辦法排 task 執行的話就是依照題目的廢棄這個 task
            if after:
                server = heapq.heappop(after)
            elif before:
                server = heapq.heappop(before)
            else:
                # All servers are busy.
                continue

            # 紀錄執行的 server
            requests_handled[server] += 1

            # 更新 server 的運作狀態以及時間
            finish_time = start + duration
            heapq.heappush(busy, (finish_time, server))

        max_requests = max(requests_handled)

        return [
            server
            for server in range(k)
            if requests_handled[server] == max_requests
        ]
