# 算 hamming distance，也就是去算二進制的數字兩兩之間相差多少(1跟0)
# 做法就是變成二進位後再去算乘法相加
# 假設其中某個位元有 m 個 0 跟 n 個 1，那總共不一樣的數量就是 m * n
# 所以就把所有的算出來就好ㄌ

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        M = max(nums)
        L = len(bin(M)[2:])
        res = 0
        val = [0] * L
        for num in nums:
            b = bin(num)[2:].zfill(L)
            for idx in range(L):
                val[idx] += int(b[idx])

        for idx in range(L):
            res += val[idx] * (n - val[idx])

        return res

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return sum( b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format,nums)))
