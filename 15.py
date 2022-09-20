# 這題是要找三個數字相加是0的，並回傳符合的數字組合，每個數字皆不能重複使用
# 做法是先做排序再用 two pointer，然後逐個數字開始找看看有沒有符合的
# 中間有用到 while 來跳過重複出現的值的計算，稍微加速一下下
# 另一種作法就是另外宣告一個 set 來儲存重複出現過的值以及一個 seen 的字典來儲存看過的值和該值用在第幾輪次，避免後面輪的值用到前面輪的值造成重複使用的問題
# 最後就做確認看看有沒有該輪次出現在 seen 裡面有缺少的值

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l<r:
                v = nums[i]+nums[l]+nums[r]
                if v == 0:
                    ans.append((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif v > 0:
                    r -= 1
                elif v < 0:
                    l += 1
        return set(ans)
