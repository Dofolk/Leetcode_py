# 這題是給一個2D陣列，然後水平垂直對分，共分成4部分，然後去看看每個部分有沒有一樣，最後做出一個四叉樹
# 做法就是遞迴，先確認要做的範圍合法之後，再去確認每個植有沒有一樣，當遇到不一樣時直接跳出往下一層去做

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.help(grid, 0, 0, len(grid)-1, len(grid[0])-1)

    def help(self, grid, rowStart, colStart, rowEnd, colEnd):
        if rowStart > rowEnd or colStart > colEnd:
            return None
        isLeaf = True
        val = grid[rowStart][colStart]
        for i in range(rowStart, rowEnd + 1):
            for j in range(colStart, colEnd + 1):
                if grid[i][j] != val:
                    isLeaf = False
                    break
            if not isLeaf:
                break
        
        if isLeaf:
            return Node(val == 1, True, None, None, None, None)
        rowMid = (rowStart + rowEnd) // 2
        colMid = (colStart + colEnd) // 2
        topLeft = self.help(grid, rowStart, colStart, rowMid, colMid)
        topRight = self.help(grid, rowStart, colMid + 1, rowMid, colEnd)
        bottomLeft = self.help(grid, rowMid + 1, colStart, rowEnd, colMid)
        bottomRight = self.help(grid, rowMid + 1, colMid + 1, rowEnd, colEnd)
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        
