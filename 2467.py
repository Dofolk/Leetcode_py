# 這題是給一個點編號從 0 到 n - 1 的無向樹圖 edges，Alice 在 node 0 出發走到所有最末端點，Bob 在 node bob 出發走向 node 0
# 還有給一個 amount 紀錄每個點該付出或是淨賺多少錢，當 Alice 跟 Bob 走過之後就一定要帶走該點所有的支出或收入
# 但是當 Alice 跟 Bob 相遇之後就把相遇點的支出收入對半分，然後問最後 Alice 最後最多可以有多少淨收入
# 做法就是先把 tree 做出來，然後用一個 list 紀錄 Bob 對於每個點的距離是多少，以及只記錄走到 node 0 的路徑
# 接著對於 Alice 做 DFS，如果 Alice 走的路徑長 depth 比 Bob 過來的距離還短的話就直接把 amount 的點的內容給吃下來
# 如果兩個人走的長度一樣，就是相遇了，這樣就可以對半分，等路徑長度的問題處理好之後就可以來確認總共的收入
# 如果走到了最末端點(tree 的端點只有一個時候)，就可以確認 ans 跟目前所有的收入 total_income 哪個大，就記錄起來
# 如果不是最末端點的話，就可以對相鄰點做下一次遞迴跟搜尋，但是要確認這個相鄰點是不是父節點(root)
# 最後等所有棟路徑都跑完之後就可以回傳答案了

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        tree = [[] for _ in range(n)]
        for n1, n2 in edges:
            tree[n1].append(n2)
            tree[n2].append(n1)
        
        dis_from_bob = [n] * n
        def dfs_bob(node, root, depth):
            if node == 0:
                dis_from_bob[0] = depth
                return True
            for neighbor in tree[node]:
                if neighbor != root and dfs_bob(neighbor, node, depth + 1):
                    dis_from_bob[node] = depth
                    return True
            return False
        dfs_bob(bob, -1, 0)

        tree[0].append(-1)
        ans = -inf
        def dfs_alice(node, root, depth, total_income):
            if depth < dis_from_bob[node]:
                total_income += amount[node]
            elif depth == dis_from_bob[node]:
                total_income += amount[node] // 2
            if len(tree[node]) == 1:
                nonlocal ans
                ans = max(ans, total_income)
                return
            for neighbor in tree[node]:
                if neighbor != root:
                    dfs_alice(neighbor, node, depth + 1, total_income)
        
        dfs_alice(0, -1, 0, 0)
        
        return ans
