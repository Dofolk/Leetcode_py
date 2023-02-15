# 這題是給一個數字 n，然後把 1 ~ n 做字典序列排序(1,10,2,3,4,5,6,7,8,9)
# 作法有兩個，一個是全部跑一遍，然後先從1 10 100 開始做，等超過 n 的時候就除回來後 +1 做 11 等的
# 另一個是另外 call 函數逐序製作好後加進去，一直做到最後

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        cur = 1
        ans = list()
        for i in range(n):
            ans.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while not cur % 10:
                    cur //= 10
        return ans


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = list()
        if n < 10:
            return list(range(1, n+1))
        for i in range(1,10):
            res.append(i)
            res += self.helper(i, n)
        return res

    def helper(self, start, n):
        res = []
        for aux in range(10):
            new = start * 10 + aux
            if new > n:
                break
            res.append(new)
            res += self.helper(new, n)
        return res
