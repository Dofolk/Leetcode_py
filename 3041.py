# ===== Question =====
# 給定一個正整數陣列 nums，每個元素都可以保持原值或加一。
# 調整後，從陣列中選出一些元素，使它們由小到大排序後，相鄰兩數都恰好差 1。
# 回傳最多可以選出幾個元素。

# ===== Thoughts =====
# 因為要計算的是有序遞增的，所以第一步一定是先把 nums 給排好再去挑選要的元素
# DP 
# 先將 nums 由小到大排序，令 dp[v] 表示用已處理的元素能組出的、以 v 結尾的最長連續序列長度，初始值皆為 0。
# 若把目前的 x 加一，就能接在以 x 結尾的序列後面，因此更新 dp[x + 1] = dp[x] + 1。
# 若保留 x，就能接在以 x - 1 結尾的序列後面，因此更新 dp[x] = dp[x - 1] + 1。
# 必須先更新 dp[x + 1]，讓它讀到上一輪的 dp[x]，才不會讓同一個元素先當 x、又當 x + 1 被算兩次。
# 處理完所有元素後，回傳 max(dp.values())，就是能選出的最長連續序列長度。
# Two Parameters 
# 將 nums 排序後逐一處理，keep 和 bump 分別記錄以剛處理的數 last 和 last + 1 結尾的最長連續序列長度。
# 處理下一個 x 時，保留 x 需要接在 x - 1 後面，把 x 加一則需要接在 x 後面，所以只要看 x 和 last 差多少。
# 差 0 時，重複的 x 無法延長以 x 結尾的序列，因此 keep 不變，但可以把這個 x 加一接在舊 keep 後面，得到 bump = keep + 1。
# 差 1 時，x 剛好能接在 last 後面，x + 1 也剛好能接在 last + 1 後面，所以 keep 和 bump 各加一。
# 差 2 時只有 x 能接在 last + 1 後面，因此新 (keep, bump) = (舊 bump + 1, 1)；差得更大時兩者都從 1 開始，而所有輪次出現過的最大長度就是答案。

# Method 1 - Sort + DP
class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        dp = defaultdict(int)  # dp[x]: the longest run ending at x
        for x in sorted(nums):
            dp[x + 1] = dp[x] + 1  # bump
            dp[x] = dp[x - 1] + 1  # keep
        return max(dp.values())

# Method 2 - Sort + Two parameters keep value
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        best = keep = bump = 1
        last = -5
        
        for num in nums:
            match num - last:
                case 0: # num repeat
                    bump = keep + 1
                case 1:
                    keep, bump = keep + 1, bump + 1
                case 2:
                    keep, bump = bump + 1, 1
                case _:
                    keep = bump = 1
            
            best, last = max(best, keep, bump), num
        
        return best
