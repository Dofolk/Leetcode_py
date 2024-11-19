# 題目是說給一個常數 array，去找出固定長度 k 的不重複數值 subarray 總和最大是多少
# [1,2,4,4,4]最大就是[1,2,4]，[2,4,4]跟[4,4,4]都有重複值所以不計算
# 做法就是用 sliding window + hash table，所以一開始就先把需要的常數都拿好，同時訂一個 begin 當成 window 的頭
# 然後開始做 for loop 跑一遍全部的東西，首先確認現在 for (sliding的概念)跑到的位置數值有沒有在 hash set裡面，沒有的話就加進去並把值加上去總和
# 接著確認有沒有達到長度 k，有的話就更新一下 begin 的位置跟最大值 M，把 sum - begin value，然後再讓 begin + 1 做移動(sliding)
# 而當數值遇到重複的時候就代表說我這個 subarray 需要重新整理，把 begin 的位置用 while 移動到重複值的位置後面，以此來排除重複的 subarray(sliding)

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        L = len(nums)
        S = set()
        M = 0
        current_sum = 0
        begin = 0
        
        for end in range(L):
            if nums[end] not in S:
                current_sum += nums[end]
                S.add(nums[end])
                if end - begin + 1 == k:
                    if current_sum > M:
                        M = current_sum
                    current_sum -= nums[begin]
                    S.remove(nums[begin])
                    begin += 1
            else:
                while nums[begin] != nums[end]:
                    current_sum -= nums[begin]
                    S.remove(nums[begin])
                    begin += 1
                begin += 1
        return M
