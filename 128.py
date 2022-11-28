# 這題是給定一串未排序的數字，找出裡面最長的連續數列長度是多少
# 做法就是先轉換成set，然後pop一個數字出來，從該數字往後找看有沒有湊成連續數列的值，找完之後換往前，最後在更新最長的長度就可以了

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        M = 0
        while nums:
            n = nums.pop()
            i = n+1
            l1 = 0
            l2 = 0
            
            while i in nums:
                nums.remove(i)
                i += 1
                l1 += 1
            i = n-1
            while i in nums:
                nums.remove(i)
                i -= 1
                l2 += 1
            M = max(M, l1+l2+1)
        
        return M
