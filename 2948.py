# 這題是給一個數字 list 跟 限制範圍 limit，然後可以做的是：如果兩個數字相差在 limit 內，就可以做數字的交換
# 問，如何可以做到整個 list 在字典序上是最佳的 list
# 做法就是去做分組，可以在 limit 內做交換的數字都給他組成一組，這邊就是用 sort 來找這些組別
# 從排序之後的 list 裡面，逐個去找跟分組，可以把排序好的 sort_nums 分成 N 個組別，對於每個數字都有 map 可以將其對應倒是哪個組的
# 同時，在分組的時候也可以順便紀錄一下，每個組別的開頭 index 是在 sort_nums 裡面的哪裡
# 等這些都做完之後，就可以去找原始 list 內的數字，透過前面尋找 map 降組別快速找出來
# 有組別之後就去看開頭在哪裡，把開頭的數字放進 result 裡面，最後在把開頭的 index 往後移一格就可以了

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sort_nums = sorted(nums)
        prev_val = sort_nums[0]
        val_to_group = {}
        curr_group = 0
        group_start = [0]
        
        for idx, num in enumerate(sort_nums):
            if num > prev_val + limit:
                curr_group += 1
                group_start.append(idx)
            
            val_to_group[num] = curr_group
            prev_val = num
        
        res = []

        for val in nums:
            group = val_to_group[val]
            res.append(sort_nums[group_start[group]])
            group_start[group] += 1
        
        return res
