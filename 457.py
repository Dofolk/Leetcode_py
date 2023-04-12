# 這題是給一個數字列表，代表這是從目前的 index 往前(負數)或往後(正數)的距離，然後找看看有沒有迴圈(都要同方向)
# 做法就是整個走一遍，然後用起頭的字元取代掉目前位置的值，代表說過了也沒有迴圈，然後就可以檢查有沒有同方向(正負相乘)以及沒有自己轉回自己
# 檢查完之後就開始換值、確認下一步位置，最後再看看有沒有走到同樣的字元標記

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        L = len(nums)
        for i, num in enumerate(nums):
            mark = str(i)
            while isinstance(nums[i], int) and (num * nums[i] > 0) and (nums[i] % L != 0):
                step = nums[i]
                nums[i] = mark
                i = (i + step) % L
            if nums[i] == mark:
                return True
        return False
