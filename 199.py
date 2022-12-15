# 這題是給一個樹，然後輸出從右邊看樹的時候會看到哪些值
# 做法就是用 level inorder 找出所有層的東西，然後蒐集最後一個就可以了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
         
        def sol(root, lv):
            if root is None:
                return
            if len(res)<=lv:
                while len(res)<=lv:
                    res.append([])
            sol(root.left, lv +1 )
            res[lv].append(root.val)
            sol(root.right, lv + 1)
        
        sol(root,0)
        ls = []
        for i in res:
            ls.append(i[-1])
        return ls
