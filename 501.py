# 這題是要找 BST(binary search tree) 中出現最多次的數字是多少
# 這邊用到 python dictionary 的一些內建函式
# 先見一個空的 dict()，然後走遍所有的節點並記錄每個節點的數值，最後用 values() 來找最大值，然後再從 dict() 裡面用 items() 取出每個元素取值看是不是最大的那個


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = dict()
        def dfs(root):
            if not root:
                return 
            if root:
                freq[root.val] = freq.get(root.val, 0) + 1
                dfs(root.left)          
                dfs(root.right)
        dfs(root)
        M = max(freq.values())
        return [x[0] for x in freq.items() if x[1]==M]
