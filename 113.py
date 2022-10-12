# 這題是要找 tree 的路徑加起來剛好是目標值的，然後回傳路徑
# 做法就是用遞迴式來做，確認好沒有超過目表以及是leaf就可以了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def sol(root, remain, ls):
            if root:
                if remain == root.val and not root.left and not root.right :
                    ls.append(root.val)
                    res.append(ls)
                sol(root.left, remain-root.val, ls+[root.val])
                sol(root.right, remain-root.val, ls+[root.val])

        sol(root, targetSum, [])
        return res
    
    
