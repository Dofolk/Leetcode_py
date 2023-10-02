# 這題是給一個數字列表，然後找出按照排序的狀況下最大的前後項差值是多少，整個操作在線性時間內( O(n) )
# 直接照著做就好，先 sort 然後在走一遍就可以了(Python比較簡單)
# 一班來說應該會先用 bucket sort 再找數字

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        M = 0
        for i in range(len(nums) - 1):
            val = nums[i + 1] - nums[i]
            if M < val:
                M = val
        return M
