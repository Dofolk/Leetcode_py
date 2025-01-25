# 這題是給一個有向圖，對於每個節點都會跟你說下一個節點可以走去哪裡，問：那些節點是可以好好地走一條路，而不是走圈圈
# 想法是用 dfs + memory，用 DFS 來找出會不會是 cycle，同時透過 memory 來記憶說如果是 cycle 的話這裏面的點有哪些，下次遇到就可以直接跳過
# 所以 dfs 這邊要去找"這條路有沒有安全？"，還傳 True 代表這個路徑是安全的沒有 cycle，反之亦然
# DFS 裡面就會判斷說，如果有曾經遇到過這個點，就去看看這個點有沒有在 path 出現過，有出現過就是不安全，回傳 False
# 沒出現過就是暫時安全，然後記錄下來說這個點有遇過，而且在 path 裡面也記錄下來
# 接著就聰這個點出發往下去走看看，當走完所有後面的路時都沒有壞掉，代表說這個點是安全的，她通下去的每條路都不會有 cycle
# 這時候就可以把路經內的點拿出來，並且標記該點安全
# DFS 設計完畢之後，就直接跑遍所有點就完成了

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        L = len(graph)
        visited = [False] * L
        path = [False] * L
        safe_nodes = set()

        def dfs(idx):
            if visited[idx]:
                return not path[idx]
            visited[idx] = True
            path[idx] = True
            for next_node in graph[idx]:
                if not dfs(next_node):
                    return False
            path[idx] = False
            safe_nodes.add(idx)
            return True
        
        for idx in range(L):
            if not visited[idx]:
                dfs(idx)
        
        return sorted(safe_nodes)
