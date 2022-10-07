# 這題是給 inorder 跟 preorder，然後把 tree 給建出來
# 這邊做法就是透過 preorder 給出層數及偏左邊的節點，然後用 inorder 從左邊開始先建立起來
# 所以一開始的時候先確認一下 inorder 有沒有東西，因為這邊的 preorder 是拿來得知層數的資訊，inorder 則是確認目前這層的左子樹還有沒有東西要擺
# 當inorder有東西的時候就代表左右子數還需要做擺放，這時候就從 preorder 拿東西出來，看看目前點是哪個，把點擺好之後就開始找子樹
# 因為已經擺好了節點，所以在目標值之前的 inorder 就會是代表這些留下的東西全都在這個目標值的左子樹裡面，右子樹亦然
# 所以就重複做一次左右子樹的建立好

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            idx = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[0:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])
            return node
        
