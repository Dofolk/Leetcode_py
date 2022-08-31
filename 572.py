# 這題給了兩個 tree，然後要判斷有沒有 subtree 的關係
# 做法就是分別把 tree 做成 list，然後去看看有沒有 sub string 的關係

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def seri(root):
            stack = [root]
            output = ','
            # 避免說 「'2' 是 '12' 的 sub string」 這狀況出現，所以在每個開頭都給他加上一個逗號以確保這狀況
            while stack:
                cur = stack.pop()
                if cur:
                    output += str(cur.val) + ','
                    stack.append(cur.right)
                    stack.append(cur.left)
                else:
                    output += '*,'
                
            return output
        
        tree = seri(root)
        subtree = seri(subRoot)
        
        return subtree in tree
        
