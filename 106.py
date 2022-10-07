# 這題是給 inorder 跟 postorder 來建出樹
# 做法就是用 postorder先建好最右邊的樹，然後在逐個往上長
# 要直接傳整個 list 來用或是用 index 傳入的方式都可以，反正能夠定位到就可以了
# 想法也跟 105 差不多，可以過去那邊看比較詳細的說明(雖然不一定看得懂)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            idx = inorder.index(postorder.pop())
            node = TreeNode(inorder[idx])
            node.right = self.buildTree(inorder[idx+1:],postorder)
            node.left = self.buildTree(inorder[:idx],postorder)
            return node
          
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        v2i = {val: idx for (idx, val) in enumerate(inorder)}
        
        def sol(l, r):
            if l>r: return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            root_idx = v2i[root_val]
            root.right = sol(root_idx + 1,r)
            root.left = sol(l, root_idx-1)
            return root
         
        return sol(0, len(inorder)-1)
