# 這題給了一個二元搜尋樹(BST)，在樹中有兩個檢的位置互換了，然後要把他們換回來
# 做法就是用 inorder traversal 來找看看
# 因為 inorder 配合上 BST 的特性，在正常情況下會按照大小順序走出來
  # 但是如果有地方互換了就會找到有問題的點，也就是前一個數字比後一個數字還大的地方，這時候就可以先記錄下第一個交換的點
  # 後面再去找另一個也是一樣狀況的就知道哪兩個點要互換了
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = pred = None
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right
        
        x.val, y.val = y.val, x.val
