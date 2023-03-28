# 這題是給一個 binary search tree，然後移除特定的節點之後重新整理整個樹
# 做法就是找點，然後確認左右邊有沒有東西，如果缺了一邊的話直接做回傳就可以了
# 都沒有缺的話就往右邊找最小的值做替換，然後再把右邊的子樹做整理就可以了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            
            if root.left == None:
                tmp = root.right
                root = None
                return tmp

            if root.right == None:
                tmp = root.left
                root = None
                return tmp
        
            tmp = self.minNode(root.right)
            root.val = tmp.val
            root.right = self.deleteNode(root.right, tmp.val)
        
        return root
    
    def minNode(self, root):
        cur = root
        while cur.left:
            cur = cur.left
        return cur
