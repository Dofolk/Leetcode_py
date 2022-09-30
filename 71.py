# 這題是要把 path 修改好，依據 linux 的標準處理
# 遇到 .. 就返回上一層，遇到 '' 或 '.' 就跳過
# 所以做法就是用一個回圈跑遍 path.split('/') 裡面的東西來判斷說有沒有需邀存起來的路徑
# 最後把路徑輸出就可以了

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split('/'):
            if i in ('','.'):
                pass
            elif i == '..':
                if stack: stack.pop()
            else:
                stack.append(i)
        return '/'+'/'.join(stack)
