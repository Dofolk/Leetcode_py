# 這題是要找 4 sum
# 作法就是降階去找，定義個 ksum 的函數，需要有數字列、目標值跟 k 是多少，最後降階到 k=2 的時候就開始做 twoSum
  # ksum 的做法就是先確認進來的數字列表有沒有問題，如果是0就直接回傳空的
    # 然後就來確認一下目標平均值有沒有比最大的大或是比最小的小，有的話直接回傳空的，因為這狀況怎麼找都不會有結果的
    # 接著確認 k 是不是 2，是的話就直接回傳 twoSum的結果
    # 最後就是開始找了，用 for 開始一個一個找，如果是第一個數字(index=0)的話就往下 call 一次 k-1 的 ksum 函數，然後用 for 把 k-1 Sum 的結果存起來
    # 如果數字跟前一個數字不一樣的話就一樣往下 call 一次 k-1 的 ksum 函數，然後一樣把結果存起來
    # 如果數字跟前一個數字一樣的話就不用做了，因為前一個數字已經做過了，而且前一個數字的可取用範圍比較大，一定比後一個數字的結果好
  # twoSum 的作法有兩種，一是 two pointer，二是用 hash set
    # two pointer 的做法就是設定左右邊界然後開始內縮找目標值，如果有找到就存起來，縮到最後沒得縮的時候就可以回傳了
    # hash set 的做法就是宣告一個 set 來記錄看過的值(用來之後找差值用的)，然後確認現在有的組數跟有沒有遇到重複的值
      # 沒有組數的時候就操作看看現在的值跟目標差多少，有沒有在 set 裡面，有的話就存起來，沒有的話就記錄到 set 裡面，在進行下一輪
      # 還要確認相同的值有沒過，從 res 裡面看看最新一筆資料的第一個數字有沒有跟現在的一樣，有的話就跳過，因為之前做過了，沒有的話就跟上一行一樣操作
      # 最後就可以得到所有的結果並回傳

# 1
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums, target, k):
            res = []
            
            if not nums:
                return res
            
            avg = target//k
            if avg < nums[0] or avg > nums[-1]:
                return res
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k-1):
                        res.append([nums[i]] + subset)
            return res
        
        def twoSum(nums, target):
            res = []
            l, r = 0, len(nums) - 1
            
            while l < r:
                s = nums[l] + nums[r]
                if s < target or (l>0 and nums[l]==nums[l-1]):
                    l += 1
                elif s > target or (r<len(nums)-1 and nums[r]== nums[r+1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            
            return res
        
        nums.sort()
        return kSum(nums, target, 4)
# 2
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums, target, k):
            res = []
            
            if not nums:
                return res
            
            avg = target//k
            if avg < nums[0] or avg > nums[-1]:
                return res
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k-1):
                        res.append([nums[i]] + subset)
            return res
        
        def twoSum(nums, target):
            res = []
            s = set()
            
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                    s.add(nums[i])
            
            return res
        
        nums.sort()
        return kSum(nums, target, 4)
