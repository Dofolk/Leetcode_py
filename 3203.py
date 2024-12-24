# 這題是給兩個無向無環的樹，然後從中各選定一個節點用一條編合併起來，問合併後樹的 diameter 最小是多少，就是在問選哪個點作合併
# diameter 就是整個樹裡面最長的那條路徑
# 所以就用 dfs 來尋找，先把 edges 變成鄰居索引清單，然後開始 dfs
# dfs 做的事情就是，先確認節點有沒有跟來源節點一樣，有就跳過沒有就往下去找更下層的
# 然後找到更下層的 diameter 跟最深的深度之後，先更新 diameter，看看往下的子樹有沒有更長的 diameter
# 接著就來比較看看 diameter 跟第一二長的子樹長度誰比較大，輝需要第一二長的原因是因為你可以用這兩個加原始節點，就可以湊出一條了
# 更新完最大值之後就開始在更新一次 diameter，因為你不知道這個 diameter 跟上面湊出來的這一條誰比較長
# 最後更新完後回傳就好了
# 最後的最後要回傳最終答案時需比較各自的最長長度及從中截斷的長度

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        neighbor1, neighbor2 = [[] for _ in range(len(edges1) + 1)], [[] for _ in range(len(edges2) + 1)]
        for a, b in edges1:
            neighbor1[a].append(b)
            neighbor1[b].append(a)
        for a, b in edges2:
            neighbor2[a].append(b)
            neighbor2[b].append(a)
        
        d1, _ = self.dfs(-1, 0, neighbor1)
        d2, _ = self.dfs(-1, 0, neighbor2)
        
        return max(d1, d2, ceil(d1 / 2) + ceil(d2 / 2) + 1)
    
    def dfs(self, parent_node, current_node, neighbors):
        max_depth1 = max_depth2 = (0)
        diameter = 0
        for next_node in neighbors[current_node]:
            if next_node == parent_node:
                continue
            child_diameter, depth = self.dfs(current_node, next_node, neighbors)
            depth += 1
            
            diameter = max(diameter, child_diameter)

            if depth > max_depth1:
                max_depth2 = max_depth1
                max_depth1 = depth
            elif depth > max_depth2:
                max_depth2 = depth
                
            diameter = max(diameter, max_depth1 + max_depth2)
                
        return diameter, max_depth1
