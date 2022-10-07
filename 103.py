# 這題是要把 tree 依層數做 zigzag
# 第一個做法比較簡單，直接找出所有層然後跳著做反轉就可以了
# 第二個做法就是一層一層做下去，每層就記錄點的順序，然後在依照正反轉放值就可以了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def sol(root, lv):
            if root is None: return
            if len(res)<=lv:
                while len(res)<=lv: res.append([])
            sol(root.left, lv+1)
            res[lv].append(root.val)
            sol(root.right, lv+1)
        
        sol(root,0)
        for i in range(1,len(res),2):
            res[i].reverse()
        
        return res
      
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        lvs = [[root.val]]
        frontier = [root]
        next_frontier = []
        reverse = True

        while frontier:
            node = frontier.pop(0)
            if node.left:
                next_frontier.append(node.left)
            if node.right:
                next_frontier.append(node.right)
            if not frontier:
                if next_frontier:
                    if reverse:
                        lvs.append([x.val for x in next_frontier[::-1]])
                    else:
                        lvs.append([x.val for x in next_frontier])
                reverse = not reverse
                frontier = next_frontier
                next_frontier = []
        return lvs
