# 這題是給一個 tree，然後對於每層做排序，由左至右由小至大，要整個樹這樣操作下來最少需要做多少次 swap
# 做法就是做 bfs，取得每一層的數字後開始做排序，排序的方式是循環的，最爛的方式就是全部走一遍，也會回到起始點
# 排序的方式就是用一個拜訪過的 visit 來記錄已經走過的節點，以及用數值+位置來做排序，依照數字大小來做位置排序
# 接著對於位置編號做 Swap，對於一個位置，先確認有沒有走過，有走過就跳過不理，因為那條環的路徑已經走完了
# 如果沒走過就開始走一遍，將所有可能的路徑走完，直到遇到曾經走過記錄在 visit 的位置
# 另一種想法就是，可以把最小獲最大的往旁邊丟，丟一次就計數一次，直到排好為止，有點 bubble sort 的想法，只是不是做雙重迴圈，只是做點對點的數值交換

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        stack = deque([root])
        ans = 0
        while stack:
            values = []
            for _ in range(len(stack)):
                node = stack.popleft()
                values.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            L = len(values)
            idx = sorted(range(L), key = lambda x: values[x])
            ans += L
            visit = [False] * L
            for i in idx:
                if visit[i]:
                    continue
                while not visit[i]:
                    visit[i] = True
                    i = idx[i]
                ans -= 1
        return ans
