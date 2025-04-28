# === Description ===
# 這題會給一個數字 list nums 跟一個數字 k，要問有多少個 subarrays(連續子集) 符合條件
# 要求的條件是， sum(subarray) * len(subarray) < k
# 
# === Thought ===
# 這題因為是要找"區間總和"以及"區間長度"的乘積，所以可以從這兩個部分下去發想
# 區間長度的部分可以選用 sliding window 來處理，者以隨時獲取當下 subarray 的長度
# 區間總和的部分可以使用 prefix sum 來做，透過 prefix 相減獲得區間的總和
# 所以這邊用一個 prefix 來記錄目前的總和，用 p1 來當 sliding window 的左邊界位置
# 這邊額外使用一個 score_len 來記錄目前 subarray 的長度，以及最後的結果 count
# 接著就是對 nums 的數字逐一記錄，先加進 prefix 之後再延伸 score_len 的長度
# 然後去判斷條件有沒有符合，有符合就不去移動 p1 的位置，不符合就去移動 p1 讓 subarray 符合條件
# 移動時要做 prefix - 1, score_len - 1 跟 p1 + 1，score_len - 1 的部分可以從 subarray 數量的計算集 sliding window 的移動過程去發想
# 接著就可以把結果記錄下來
#
# === Code ===
#
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix, p1, count, N, score_len = 0, 0, 0, len(nums), 0

        for num in nums:
            prefix += num
            score_len += 1
            
            while prefix * score_len >= k:
                prefix -= nums[p1]
                score_len -= 1
                p1 += 1
            count += score_len
        
        return count
