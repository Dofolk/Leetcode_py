# 這題是給兩個數字 list，裡面是數字 1~n shuffle，然後看看 prefix 的長度內有幾個共通的數字，並且從頭記錄到尾
# 也就是從 index = 0 開始計算
# 做法就是用兩個長度更長一點的 list 來記錄有沒有走過，走過就計數，沒走過就標記成有走過
# 透過多開空間來換時間，因為原始的 list 裡面就是數字了，所以直接透過數字為製作訪問跟取值就可以了

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        L = len(A)
        ans = [0] * L
        seenA, seenB = [0] * (L + 1), [0] * (L + 1)
        count = 0
        for idx in range(L):
            count += seenA[B[idx]] + seenB[A[idx]]
            if A[idx] == B[idx]:
                count += 1
            ans[idx] = count
            seenA[A[idx]] = 1
            seenB[B[idx]] = 1
        return ans
