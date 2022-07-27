# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def bt(L,R):
            if L>R:
                return None
            p = (L+R)//2
            
            root = TreeNode(nums[p])
            root.left = bt(L, p - 1)
            root.right = bt(p + 1, R)
            return root
        return bt(0,len(nums)-1)
      
# 用遞回來做出二元分類樹
# 設計遞迴是的時候考慮最簡單的3個點做分類就可以了
# 要注意到邊界要放多少進去，還要設計一個return None來停止遞迴
