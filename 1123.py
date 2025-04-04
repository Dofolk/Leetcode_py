# === Description ===
# 這題是給一個 tree，然後問最深的葉子節點們的共同祖先是誰？

# === Thought ===
# 題目非常的簡潔，可以知道說要找"最深"的節點們的祖先，所以這裡就先從怎麼確認每個節點深度去想
# 因為是 tree 的結構再加上要找深度，所以可以從 DFS 著手，首先是當傑點不存在，那就直接回傳深度就好
# 接下來左右兩邊的子節點下去尋找，拿到左右兩遍 subtree 的最深有多深
# 如果同樣深度就代表說我這個節點是祖父節點，不同深度的話就知道說祖父節點是在更上層
# 但祖父節點有機會很多個(有確認到祖父節點就知道說往上去所有點都是祖父節點)，這樣變成要多補一點東西來確認誰才是最深的祖父節點
# 這邊就讓 dfs 多做參數回傳，因為 dfs 深掘的特性，所以可以讓回傳參數多傳一個節點資訊
# 如果節點不存在就是回傳 None，然後在每一個點比較左右子樹的深度時，依照深度去回傳左或右子樹的節點資訊
# 如果說左右子樹深度一樣就代表目前的節點就是祖父節點，這樣的話就回傳當前的節點跟深度就可以了


# === Code ===

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, depth):
            if not node:
                return (None, depth)
            left, left_depth = dfs(node.left, depth + 1)
            right, right_depth = dfs(node.right, depth + 1)
            
            if left_depth > right_depth:
                return (left, left_depth)
            elif right_depth > left_depth:
                return (right, right_depth)
            else:
                return (node, left_depth)
        
        ans, _ = dfs(root, 0)
        return ans
