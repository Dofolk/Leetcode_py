# 這題是給一堆 pair 代表一個編的兩端數字，這會構成一個 tree，然後找看看誰們當 root 的時候可以獲得的 tree 有最小的高度
# 想法就是從葉子端開始做修剪，剪到最後就剩下最內層的東西就是可以當成root的點們了
# https://leetcode.com/problems/minimum-height-trees/solutions/76055/share-some-thoughts/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        leaf = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaf)
            newLeaf = []
            for l in leaf:
                j = adj[l].pop()
                adj[j].remove(l)
                if len(adj[j]) == 1: newLeaf.append(j)
            leaf = newLeaf
        
        return leaf
            
