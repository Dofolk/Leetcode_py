# 這題是要從一個 rotated 的非遞減序列找出目標值有沒有存在
# 作法就是用二元搜尋，但是在做搜尋之前先把搜尋指標做一詞更新
# 因為這次的題目沒有說值是唯一的，所以有可能會出現重複的值，這樣的話就先做個左右兩邊的搜尋指標更新
# 最後就直接跟之前的題目一樣做就好了

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        l, r = 0, len(nums) - 1
        
        while l<=r:
            while l < r and nums[l] == nums[l+1]:
                l += 1
            while l < r and nums[r] == nums[r-1]:
                r -= 1
            
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[l]<=nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False
