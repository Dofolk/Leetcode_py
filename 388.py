# 這題是給一串代表檔案路徑得字串，然後找出路徑最長的路徑最多有幾個字母
# 做法就是用 split() 來做分割，先做出每個節點在哪，然後再用一次 split() 來把每個點的 \t 轉成階層數
# 轉換好之後就可以把結果弄成 tuple 加到 stack 保存起來，然後之後遇到階層比較低的代表已經換了一個上層的節點，就把 stack 的東西丟出來直到階層符合
# 最後再確認 '.' 有沒有在裡面，有代表是最後了，那就可以更新 answer 了

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths, stack, ans = input.split('\n'), [], 0
        for path in paths:
            p = path.split('\t')
            depth, name = len(p) - 1, p[-1]
            L = len(name)
            while stack and stack[-1][1] >= depth:
                stack.pop()
            if not stack:
                stack.append( (L, depth) )
            else:
                stack.append( (L + stack[-1][0], depth) )
            if '.' in name:
                ans = max(ans, stack[-1][0] + stack[-1][1])
        return ans
