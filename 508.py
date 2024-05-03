# 這題是給一個二元樹，然後去統計各個子樹的數字和頻率最高的是那些數字
# 作法就是用 default dictionary 來記錄子樹總和，配合上 DFS 把節點的子樹往上做總和整理
# 所以就先宣告 defaultdict，然後定 dfs 的函數，最後找 default dictionary 出現次數最多的鈉些數字輸出就好了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        D = collections.defaultdict(int)
        
        def cal_val(node):
            if not node:
                return 0
            val = node.val + cal_val(node.left) + cal_val(node.right)
            D[val] += 1
            return val
        
        cal_val(root)
        M = max(D.values())
        
        return [k for k, v in D.items() if v == M]
