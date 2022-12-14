# 這題是給一串數字，然後要做 k 個 rotate
# 做法就是先做 mod，確保 k < len(nums)，然後各自賦值就可以了

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _, k = divmod(k, len(nums))
        if k == 0: return
        nums[:k], nums[k:] = nums[-k:], nums[:len(nums)-k]
