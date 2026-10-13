# ===== Question =====
# 題目會給一個數字 list nums，然後可以任意調換數字的位置，最後回傳最大交替平方差和是多少
# 交替平方差和 = nums[1]^2 - nums[2]^2 + nums[3]^2 - nums[4]^2 + ...

# ===== Thoughts =====
# 這題說可以任意調換位置以及交替平方差和會有必定正數的減法
# 所以就是要提高加法的數值並降低減去的數值，所以就是去做排序(因為可以任意調換位置，所以可以隨意安排)
# 然後最大的一半是要做加法，剩下另一半就分配給減法，這樣就可做到最大的和

# Method - Square Sort
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(num * num for num in nums)
        half = len(nums) // 2
        return sum(sq[half:]) - sum(sq[:half])
