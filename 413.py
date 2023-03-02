# 這題是給一個序列，然後找裡面最多有幾個等差子序列(長度要大於2)
# 做法就是一個來記錄前面有幾個(prev)，然後還有一個計數(count)來記錄目前總共遇過幾個
# 因為後面加進來的如果也是等差，那就代表說他會比前面一個多出一個來列組合，所以先把 prev + 1，然後再加到計數上面去
# 如果沒有的話就直接清空，因為不會有子序列(連續的問題)了

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        prev, count = 0, 0
        for i in range(2,len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                prev += 1
                count += prev
            else:
                prev = 0
        return count
