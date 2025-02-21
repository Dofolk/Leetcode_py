# 這題是給一個 tree，然後一開始的 node val 都是 -1，root val 是 0，如果左子點存在的話 node val 就是父節點 val * 2 + 1，如果是右節點的話就改成 + 2
# 這樣的話，設計一個 class 來做兩件事，一是弄出 tree，二是 find() 給定的值有沒有在樹裡面
# 所以在 init 的時候就可以先把 tree 裡面出現的值都存起來
# 然後 find() 直接用 in 看有沒有存在就好

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.vs = set()
        q = deque()
        q.append((root, 0))
        while q:
            node, val = q.popleft()
            self.vs.add(val)
            if node.left:
                q.append((node.left, 2 * val + 1))
            if node.right:
                q.append((node.right, 2 * val + 2))

    def find(self, target: int) -> bool:
        return target in self.vs


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
