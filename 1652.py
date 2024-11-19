# 這題是說你要解密，會給一個常數 list 及一個數字 k，解密方法是依據數字 k 來決定每個位置要往前還是往後 k 個數字相加
# 解法是用 sliding window，，所以就是先判斷 k，大於 0 就直接做就好，小於 0 就做反向的
# 然後再做加總的時候就是做一個加一減一，減去當下的位置數字，加上往後一格的數字，這樣做可以比較快(大於sum())

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        L = len(code)
        res = [0] * L
        if k == 0:
            return res
        if k > 0:
            res[0] = s = sum(code[1:k+1])
            for i in range(1, L):
                p = ( k + i ) % L
                s += code[p] - code[i]
                res[i] = s
            return res
        
        res[0] = s = sum(code[-1:k-1:-1])
        for i in range(1, L):
            p = ( i - k ) % L
            s += code[-p] - code[-i]
            res[-i] = s
        return res
