# 這題是給一個遞增相異數列，然後切成兩段，比較大的那段擺前面，拿到一個新的數列
# 然後限制時間logn下在給定的新數列裡面找出指定的值
# 做法跟binary search類似，一樣從兩邊開始往內縮，只是要去判斷一下目前的數列是左長右短還是左短右長
# 依據中間位置的值跟target的值來判斷一下說左右界要怎麼縮

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l] > target or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
