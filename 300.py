# 這題是要從給定的序列裡面找出 嚴格遞增的最長子序列 的長度多少
# 這邊用 tail 來記錄每個長度的尾巴項最小的值是多少，有最小的尾巴項就可以擁有最長的長度，因為後面比較好找到大的值來接續著前面的子序列
# 同時，也可以透過尾巴項來看看要不要加長序列等等的
# 然後就再給定的序列裡面逐一跑過，用 size 來記錄要算多少長度的子序列，並且配合所有的尾巴項的值
# 比所有尾巴都大就 size + 1，最後回傳 size 就可以了


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i+j)//2
                if tail[m] < x:
                    i = m + 1
                else:
                    j = m
            tail[i] = x
            size = max( i + 1 , size )
        return size
