# ===== Question =====
# 題目會給一個有向加權圖 edges，每個節點都有一個字元標籤 labels，要求從節點 0 移動到節點 n-1。
# 路徑上相同字元最多只能連續出現 k 次，超過則視為不合法路徑。
# 找出所有合法路徑中，邊權重總和最小的路徑，若不存在則回傳 -1。

# ===== Thoughts =====
# 這題是再找最小路徑為基礎，再加上路徑合法的確認 => 基底可以選用 heap 找路徑之後再去確認合法性
# 這邊就先建立一個有向圖出來，並記錄每一個邊的權重是多少，然後從 0 開始 heap，並且記錄端點有沒有訪問過
# 這邊 heap 記錄三個資訊: (目前的路徑的最小權重和, 前面連續出現幾個相同的字母(合法性檢查用), 現在是哪個節點)
# 當 heap pop 直出來之後先檢查: 拜訪過？是不是最後一個節點？
# 然後就接著可以對往後指向的幾個節點做字元連續的合法性檢查以及路徑和的更新
# 所有路徑如果都跑完還沒有遇到 n - 1 回傳的話就代表沒辦法抵達終點直接回傳 -1(題目要求)

# Method - Directed Graph + Heap
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v, val in edges:
            graph[u].append((v, val))
        
        # total sum, consecutive length, current node
        heap = [(0, 1, 0)]
        visit = [False for _ in range(n)]

        while heap:
            total, conti, node = heapq.heappop(heap)
            if visit[node]:
                continue

            if node == (n - 1):
                return total

            for next_node, val in graph[node]:
                if visit[next_node]:
                    continue
                # 檢查字元連續性有沒有合法，連續出現就延續連續性 + 1，沒有連續出現就 reset 回 1(當下就是一個字元了)
                length = conti + 1 if labels[node] == labels[next_node] else 1
                if length > k:
                    continue
                # 推回 heap 等待下一次的更新
                heapq.heappush(heap, (total + val, length, next_node))
                visit[node] = True
        
        return -1
