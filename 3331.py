# ===== Question =====
# 給你一棵以節點 0 為根的樹，parent[i] 表示節點 i 的父節點，s[i] 表示節點 i 的字元。
# 每個非根節點都沿著原本的樹往上找，把最近的同字元祖先設為新父節點；找不到就保留原本的父節點，所有變更同時生效。
# 回傳一個陣列 ans，其中 ans[i] 是變更後節點 i 的子樹大小，包含它自己和所有後代。

# ===== Thoughts =====
# 這題是要去更改 tree 的嘟點，並且再去計算 subtree(含 root)的大小
# 因為要找最近的相同字元的端點去做 root 的更新，所以選擇用 DFS 把當下的每一條路都走過一輪
# 走的時候先記錄目前:遇到過那些文字以及是哪個 node 編號，當遇到重複的時候就依題目更新 root
# 最後再把每個子端點的 subtree size 加到正確的 root 底下
# 詳細步驟參考以下 comment

# Method 1 - DFS
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        # children: 紀錄每個 node 的子端點有誰
        children = [[] for _ in s]
        for node in range(1, len(s)):
            children[parent[node]].append(node)
        ans = [1] * len(s)
        # 紀錄目前有遇過的字元他最近的端點是哪一個點
        closest = dict()

        def dfs(node):
            curr_char = s[node] # 目前端點是哪個字元
            prev_node = closest.get(curr_char, -1) # 目前這個字元最近的端點是哪一個 node
            closest[curr_char] = node # 更新字元最近的端點是自己，這樣好更新 children 的端點
            # 走過每個 child 去更新他們的 root
            for child in children[node]:
                dfs(child)
            # 走完 child 之後把字元最近的端點還原成之前的端點，因為後面都更新完了就要還原回去
            # 避免在不同的大分支去交互混用到端點
            closest[curr_char] = prev_node
            # 把目前端點的 subtree size 更新進去新的 root，要確認新的 root 不是指向 -1
            # 如果是指向 -1 代表兩個狀況: 處理到 node 0 或是 前面沒有一樣的字元
            # 所以先確認 node 非 0 ，然後如果前面沒有一樣的字元的話就按照題目規則把 subtree size 加進不用更新的 parent 裡
            if node: # avoid deal with root node 0
                ans[prev_node if prev_node >= 0 else parent[node]] += ans[node]
        
        dfs(0)
        return ans
