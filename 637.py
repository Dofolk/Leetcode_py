# 這題是要算出樹的每層數值平均
# 做法就是遞回做DFS，先確認層數有沒有存在，然後再把值加進去，最後再逐層算平均

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        self.level = []
        def sol(root,lv):
            if len(self.level)==lv:
                self.level.append([])
            if root is None:
                return
            self.level[lv].append(root.val)
            if root.left:
                sol(root.left,lv+1)
            if root.right:
                sol(root.right,lv+1)
        sol(root,0)
        for idx, val in enumerate(self.level):
            self.level[idx] = sum(val)/len(val)
        return self.level
