# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while 1:
            if p.val==cur.val or q.val==cur.val:
                return cur
            elif p.val>cur.val and q.val>cur.val:
                cur = cur.right
            elif p.val<cur.val and q.val<cur.val:
                cur = cur.left
            elif p.val>cur.val and q.val<cur.val:
                return cur
            elif p.val<cur.val and q.val>cur.val:
                return cur
              
# 這題是要找給定的兩個節點 p, q ，他們倆個的最近源頭是哪個節點
# 題目提供 binary search tree 跟一定在樹裡面的兩個節點，所以只要判別有沒有要回傳或是下一步要往左右邊走就可以了
# 只要其中一個數字等於目前所在節點，回傳就對了，因為這就是最原始的點了
# 如果 p, q 嚴格大於或是小於目前節點的話就判斷往左或往右走
# 最後就是 p, q 被分成兩邊的話那就直接回傳當下節點
