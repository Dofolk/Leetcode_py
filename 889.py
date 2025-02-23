# 這題是給 binary tree 的 preorder list 跟 postorder list，然後還原成原本的 binary tree，如果可以還原成多種樣貌的 tree 的話就任一個就好
# 這邊就用 preorder 來找每個部份的 root node，再透過 postorder 來確認每次操作的時候，list 的哪個 index 是左右子樹的分界
# 然後用 recursive 的方式，往下去找就可以了
# 在每次的操作時，preorder 的第一個數字跟 postorder 的最後一個數字就是 root node 的點，所以這邊在遞迴操作的時候要掐頭去尾再往下傳遞

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        self.divide(preorder[1:], postorder[:-1], root)
        return root
    def divide(self, subtree_pre, subtree_post, root):
        if not subtree_pre:
            return
        if len(subtree_pre) == 1 and len(subtree_post) == 1:
            root.left = TreeNode(subtree_pre[0])
            return
        left_pre, left_post, idx = set(), set(), 0
        while 1:
            left_pre.add(subtree_pre[idx])
            left_post.add(subtree_post[idx])
            idx += 1
            if left_pre == left_post:
                break
        root.left = TreeNode(subtree_pre[0])
        self.divide(subtree_pre[1:idx], subtree_post[:idx - 1], root.left)
        if idx < len(subtree_pre):
            root.right = TreeNode(subtree_pre[idx])
            self.divide(subtree_pre[idx + 1:], subtree_post[idx: - 1], root.right)
        return 


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        val = postorder.pop()
        node = TreeNode(val)
        if not postorder:
            return node
        
        idx = postorder.index(preorder[1])
        node.left = self.constructFromPrePost(preorder[1: idx + 2], postorder[:idx + 1])
        node.right = self.constructFromPrePost(preorder[idx + 2:], postorder[idx + 1:])
        return node
