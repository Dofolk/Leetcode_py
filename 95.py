# 這題是要做出 1~n 的所有二元搜尋樹的可能
# 做法就是用遞回來做，先拿好root是哪個，然後再往左右下去找子樹，一直做到左右子節點都是NULL
# 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(first, last):
            trees = []
            for root in range(first, last+1):
                for left in generate(first, root-1):
                    for right in generate(root+1, last):
                        node = ListNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees or [None]
        
        return generate(1,n)
