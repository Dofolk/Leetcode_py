# 這題是要把一個數依據層數輸出
# 做法就是用 inorder 做尋訪，然後最左邊就會一個一個抓進來，這樣就沒問題了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return res
