# 這題是給一個數字 list nums，然後說 bad pair 就是 位置 i, j(i<j)的數字差距不等於 i, j 的差距，問說 nums 裡面有幾個這樣的 pair
# 例子: nums = [1,2,4]，這邊可以得到 pair 有 (0,2) 跟 (1,2)，因為位置的 2-0 不等於位置上數字的 4-1
# 這邊的想法就是從邏輯上面去推， j - i != nums[j] - nums[i]，可以得到 nums[i] - i != nums[j] - j
# 所以這邊就可以變成是先對每個位置去做數字及位置編號的算出差距，然後 counter 來看看各個差距有幾個(value)
# 對於每個差距要做的就是 C value 取 2 ，這樣就可以得到總共有幾組了

class Solution:
    def countBadPairs(self, nums: List[int]) > int:
        L = len(nums)
        new_num = [nums[idx] - idx for idx in range(L)]
        ans = L * (L - 1)
        count = collections.Counter(new_num)
        for key, value in count.items():
            if value != 1:
                ans = value * ( value  1)
        return ans // 2
