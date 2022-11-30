# 這題是給一個字串 s，然後找出所有回文的子字串，集結成一個 list 後回傳
# 做法是用 backtracking，首先判斷書入的字串有沒有東西，沒有東西代表已經可以存結果了
# 如果有東西就先檢查一個字母可不可以回文，可以就加到 path 裡面，然後把剩下的字串做下一個遞迴
# 然後再來檢查兩個字母的回文狀況，三個四個並逐個增加到全部做完

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1 ):
                if self.isPal(s[:i]):
                    backtrack(s[i:], path + [s[:i]], res)
        
        backtrack(s, [], res)
        return res
    
    def isPal(self, s):
        return s==s[::-1]
