# 這題是要做出 tree 的 in-order search，然後去設計初始化函式、next value 函式跟 次一數值存在與否函式
# 做法就是在初始化的時候先做一次 inorder search，然後再記錄一下現在的 index 在哪邊來決定有沒有下一個數值

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        def traversal(root):
            if root is None:
                return
            traversal(root.left)
            self.res.append(root.val)
            traversal(root.right)
        traversal(root)
        self.idx = 0

    def next(self) -> int:
        if self.idx < len(self.res):
            v = self.res[self.idx]
            self.idx += 1
            return v

    def hasNext(self) -> bool:
        if self.idx < len(self.res):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
