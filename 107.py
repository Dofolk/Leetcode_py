# 這題是要把 tree 由下而上，有左而右一層一層輸出
# 做法就是用遞迴來操作，輸入節點跟層級，這樣就可以做好了，最後再反向輸出就會是最底層了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        prev = [root]
        next_prev = []
        res = []
        tmp = []
        while prev or next_prev:
            node = prev.pop(0)
            tmp.append(node.val)
            if node.left: next_prev.append(node.left)
            if node.right: next_prev.append(node.right)
            if not prev:
                res.append(tmp)
                tmp = []
                prev = next_prev
                next_prev = []
                
        res.reverse()
        return res
      
      
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        res = []

        def sol(root,lv):
            if len(res) <= lv:
                res.append([])
            res[lv].append(root.val)
            if root.left:
                sol(root.left, lv+1)
            if root.right:
                sol(root.right,lv+1)
        sol(root,0)        
        return res[::-1]
