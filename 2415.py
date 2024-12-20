# 這題是給一個完美二元樹(每層所有節點都有值)，然後將奇數層的值做順序的反轉，最左邊跟最右邊互換
# 做法是做 BFS，首先確認接下來的節點有沒有東西，然後確認層數，如果是奇數就做數值交換
# 交換完畢之後就把左邊的左節點跟右邊的右節點做下一次的數值交換，這樣剛好可以把左右對應位置的點做連結並交換
# 然後再把左邊的右節點跟右邊的左節點做數值交換，這樣就可以把所有位置都對應起來把數值都交換完
# 這邊做的是數值交換，不是節點的重新連結，重新連結比較難去紀錄要怎麼連

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        def swap_val(leftnode, rightnode, level):
            if not leftnode:
                return
            if level % 2:
                leftnode.val, rightnode.val = rightnode.val, leftnode.val
            swap_val(leftnode.left, rightnode.right, level + 1)
            swap_val(leftnode.right, rightnode.left, level + 1)
        
        swap_val(root.left, root.right, 1)
        return root
