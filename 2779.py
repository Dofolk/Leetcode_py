# 這題是給一個整數 list 跟一個數字 k，每個位置的數字都可以調整為大小相差 k 之內的任一數值(i.e. [a-k, a+k]之間)，求最長可以有多長的數字可以調整成一樣的
# 做法是先 sort，排序好之後再開始逐個檢查，用 pos 來記錄位置，如果當下檢查到的數字 (num) 已經超過 pos 位置的數值時，pos 就會被拖著跟著 +1
# 這樣的做法就是動態式的 sliding window，pos num 都往前跑，遇到兩個在範圍內的時候 pos 就定著去紀錄長度，然後超過範圍之後就要跟著跑做調整以方便找到下一個區間

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        pos = 0
        K = 2 * k
        for num in nums:
            if nums[pos] + K < num:
                pos += 1
        return len(nums) - pos
