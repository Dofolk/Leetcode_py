# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 這題做tree的inorder，就是走過哪個點就給他記錄下來，然後是偏重左邊的
# 下面兩個方法
# 第一個就是ls竹個紀錄走過的點，然後用stack list來記錄接下來要走的點
# 第二個方法就是recursive，因為走過就紀錄，所以最最最一開始的時候就要先記錄了


class Solution:
  
# Solution 1  
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        stack = []
        
        cur = root
        
        while stack or cur is not None:
            while cur:
                stack.append(cur)
                ls.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
    
        return ls
    
# Solution 2
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        cur = root
        
        def travel(root):
            if root is None:
                return
            ls.append(root.val)
            travel(root.left)
            travel(root.right)
            
        
        travel(cur)
        return ls
