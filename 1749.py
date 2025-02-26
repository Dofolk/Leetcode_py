# 這題是給一個整數 list，然後問對於 subarray 來說最大可以拿到多大的總和絕對值( |sum(a_i)| )
# 要找 subarray，所以可以從 prefix 去想，要絕對值最大的話就是去看看 prefix 在哪個區間會有最大的差距
# 這個最大的差距就是最終的目標，這可以透過 prefix 的結合概念去推得
# 假設在區間 [i, j] 是目標區間，a_i + ... + a_j 其實就是 prefix_i - prefix_j
# 這樣一來題目要找最大的這個區間 [i, j] 就變成 找 prefix_i - prefix_j 最大的了，也就是 max - min
# 以上的想法套進去之後，先給三個數字分別記錄最大最小跟 prefix，每次都更新一下最大或最小值，最後回傳相減就好

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        M, m, prefix = 0, 0, 0
        for val in nums:
            prefix += val
            if prefix > M:
                M = prefix
            elif prefix < m:
                m = prefix
        return M - m
