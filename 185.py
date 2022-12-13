# 這題是給一串數字，然後把數字做個排序，讓數字串起來之後會變成最大
# 作法就是把數字變成字串，然後用 quick sort 的概念先把第 i 個給找出來(while loop)，然後再對前後兩段再做一次 sort
# 然後要把左邊的0給移除後就可以當成第一步解，然後確認下是不是長度為0(本身全部0，所以移除0的時候變成沒東西)，是就回傳0，不是就照常回傳
# 另一個方法是用 cmp ，但目前還不太熟

class Solution:
    def largestNumber(self, nums):
        result = ''.join(self.quicksort(list(map(str, nums)))).lstrip('0')
    
        if len(result) == 0:
            return '0'
        else:
            return result
    
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[i+1] < nums[i+1] + nums[i]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                i += 1
            else:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                j -= 1
                
        return self.quicksort(nums[:i]) + [nums[i]] + self.quicksort(nums[i+1:])
      
class Solution:
    def largestNumber(self, nums):
        def mycmp(x, y):
            return -1 if x + y < y + x else x + y > y + x or 0

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(mycmp), reverse=True)
        return ''.join(nums).lstrip('0') or '0'
