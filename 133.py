# 這題會給一個圖，然後把圖給複製出來。題目會給點跟他的鄰居列表，依據這個去作出一份複製圖
# 想法就是 dfs，需要兩個東西，一個是 visited，用來存走過的點，避免說一直走重複的路然後死掉
# 一個是 G，用來當複製圖的，用來存走過的點是那些以及他的鄰居列表做新增
# 設計的想法就是，先確認有沒有走過，沒走過就加到 visited，然後看看有沒有存在複製圖哩，沒有的話就先加點進去
  # 有的話就可以用一個 for 來新增新鄰居，並且順著鄰居的路徑往下找在下一個點跟鄰居列表的更新

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = set()
        G = dict()

        def dfs(n, G, visited):
            if n in visited:
                return
            visited.add(n)
            if n not in G:
                G[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in G:
                    G[neigh] = Node(neigh.val)
                G[n].neighbors.append(G[neigh])
                dfs(neigh, G, visited)
        
        dfs(node, G, visited)

        return G[node]
