# 這題是給一棵樹，然後找想要的目標總和的路徑可以有幾個
# 做法就是用 hash map 來記錄與目標的差距以及可以有幾條路徑達到這個剩餘值
# 如果總和有在 hash 裡面就紀錄多一點，沒有就更新表(用來看數值達到哪邊並記錄次數)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        hashMap = {0:1}
        self.ans = 0
        def dfs(root, targetSum, total):
            if root is None:
                return
            total = total + root.val
            remainder = total - targetSum
            
            if remainder in hashMap and hashMap[remainder] > 0:
                self.ans += hashMap[remainder]
            if total in hashMap:
                hashMap[total] += 1
            else:
                hashMap[total] = 1
            if root.left:
                dfs(root.left, targetSum, total)
            if root.right:
                dfs(root.right, targetSum, total)
                
            hashMap[total] -= 1
                    
                    
        dfs(root, targetSum,0)
        return self.ans
