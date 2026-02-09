'''
題目
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.(樹的左右子樹最深深度差距<=1)
'''

'''
題目說給一個二元搜尋樹，回傳一個平衡的二元搜尋樹(二元搜尋樹就是比root大就擺右邊，小就左邊)
首先知道的是用inorder來跑二元搜尋樹的時候，剛好可以讓整個跑的node數值遞增(因為二元搜尋樹的特性)
所以這時候就是直接把tree打掉重來就可以了，用inorder把數值依序排出來，然後再從每個區間段的中點抓起來做subtree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_list = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            node_list.append(node)
            inorder(node.right)
        
        inorder(root)

        def rebuild_tree(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = node_list[mid]
            node.left = rebuild_tree(left, mid - 1)
            node.right = rebuild_tree(mid + 1, right)
            return node
        
        return rebuild_tree(0, len(node_list) - 1)
