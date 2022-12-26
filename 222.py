# 這題是給一個 complete binary tree，然後要找有多少節點
# 做法就是去找看看現在左右子樹哪個是 full tree
# 去找左右子樹個別最左邊那條路有沒有一樣長
  # 根據 complete tree 的性質，一樣長的話代表說左子樹是個 full tree(因為可以填滿左邊滿到右邊那邊去)，所以就算左邊的 full tree node 數量再加上右邊的
  # 如果不行就是左邊不是full(最底層沒有滿)，右邊才是full，所以就是算右邊的 full tree node 數量之後再加上左邊的

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        L_dep = self.dep(root.left)
        R_dep = self.dep(root.right)
        if L_dep == R_dep:
            return pow(2, L_dep) + self.countNodes(root.right)
        else:
            return pow(2, R_dep) + self.countNodes(root.left)
    
    def dep(self, root):
        if not root: return 0
        return 1 + self.dep(root.left)
