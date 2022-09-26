# 這題是做數字序列的 permutation，然後再列出來
# 做法是用 backtrack，想法類似於 3 sum，最一開始就先把帶頭的數字交換成後面的一個，然後後面的又可以再做一樣的事情，一直交換，就可以做到所有 permutation


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        L = len(nums)
        
        def backtrack(leng):
            if leng == L:
                ans.append(nums[:])
                return
            for i in range(leng, len(nums)):
                nums[leng], nums[i] = nums[i], nums[leng]
                backtrack(leng + 1)
                nums[leng], nums[i] = nums[i], nums[leng]
        
        backtrack(0)
        
        return ans
