# 這題是要看看一串數字序列能不能走到最後
# 作法一就是直線前進，跟之前的一樣作法，照著走照著算，看看有沒有走到最遠是0，剛好也是要在0做更新
# 作法二就是回過頭來找，從最後網錢找看看前面的數字能不能走超過到目前所在的最後，可以的話就更新最後位置到前面去，重複找

class Solution:

# 1
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        current_jump_end = 0
        for i in range(len(nums)):
            farthest = max(farthest,nums[i] + i)
            if farthest == i and i != len(nums)-1:
                return False
            if i == current_jump_end:
                current_jump_end = farthest
        return True if farthest>=len(nums)-1 else False
      
# 2
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i >= last:
                last = i
        return last == 0
