# 這題是給一個 list 表示依序編號大樓的樓層數，然後給一個 query 表示兩個人分別在哪幾個編號的大樓，現在他們要相遇的話要去哪一棟樓
# 而移動的規則就是只能在"自身編號之後"的"更高的(>)"大樓存在才可以做移動，如果都沒辦法移動的話就記錄成 -1，可以移動就紀錄移動到哪棟樓去
# 想法是編號 x, y 大樓如果 x == y 或 x 的樓層比 y 的低( heights[x] < heights[y]) 時直接紀錄好 y 就好，做這部之前可以先把 x, y 做出 swap 以確保 x <= y
# 這邊就有幾個篩選: x <= y, heights[x] < heights[y], x == y，所以需要處理 x > y 跟 heights[x] >= heights[y]
# 如果沒有上面的操作時就記錄下來，接下來要準備找出 y 後面的大樓樓層高於 x 大樓的(如上)
# 這邊在尋找的時候用 monotonic decreasing stack 紀錄從樓層數最後面往前紀錄，(ex. 7->5->3...)，如果遇到更高樓層的，就直接把 stack pop 到可以放這個樓層
# 然後在找目標的時候就用 binary search 在 stack 裡找出精確的位置

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        LH, LQ = len(heights), len(queries)
        if L == 1:
            return [0]
        ans = [-1] * LQ
        new_q = [[] for _ in range(LH)]
        for idx in range(len(queries)):
            a, b = queries[idx][0], queries[idx][1]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[idx] = b
            else:
                new_q[b].append((heights[a], idx))
        
        mono_stack = list()
        def search(val, stack):
            left, right, ans = 0, len(stack) - 1, -1
            while left <= right:
                mid = (left + right) // 2
                if stack[mid][0] > val:
                    ans = max(ans, mid)
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        
        for idx in range(len(heights) - 1, -1, -1):
            mono_stack_size = len(mono_stack)
            for val, idx_q in new_q[idx]:
                position = search(val, mono_stack)
                if position < mono_stack_size and position >= 0:
                    ans[idx_q] = mono_stack[position][1]
            while mono_stack and mono_stack[-1][0] <= heights[idx]:
                mono_stack.pop()
            mono_stack.append((heights[idx], idx))

        return ans
