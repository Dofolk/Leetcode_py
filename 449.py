# 這題是給一個 binary search tree，然後自己設計一個壓縮跟解壓縮法，讓樹壓縮成字串，再從字串解壓縮回來
# 想法就是用 pre order，遇到一個就變成字元存一個，走道眉路的時候給他打上 * 來表示就可以壓縮了
# 解壓縮就改成遇到星號就加新的節點

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        tree = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                tree.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                tree.append('*')
        
        return ','.join(tree)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        tree = deque(data.split(','))
        root = TreeNode(int(tree.popleft()))
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if (left := tree.popleft()) != '*':
                node.left = TreeNode(int(left))
                queue.append(node.left)
            if (right := tree.popleft()) != '*':
                node.right = TreeNode(int(right))
                queue.append(node.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
