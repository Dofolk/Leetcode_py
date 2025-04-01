# === Description ===
# 題目會給一個 nums 的房屋價值以及至少要偷 k 家，問在偷取限制與條件下最少會偷多"少"錢
# 偷的限制是不偷相鄰的，每次至少偷 k 家，然後每次就偷這些組合裡最大的那一家，問這些所有組合的可能最小是多少

# === Thought ===
# 這題知道說結果會是其中某一家，所以這逼可以透過 binary search 來找看看
# 首先知道最大跟最小就是數列的最大跟 1，接著找中間值 mid，然後照著房屋順序重頭跑一遍
# 這邊用 while + index++ 來跑，如果房屋價值比 mid 還小的話就偷(stolen + 1)，然後 idx + 2(相鄰不偷)
# 如果比 mid 還大就不偷，因為我們是要找出最小的
# 然後等所有房子都確認過後看看要偷得有幾家，如果要偷的(stolen)數量比 k 還大，那就把上限往下調到 mid
# 代表說這個 mid 會偷太多，會有多餘的扣打可以選擇幾家不偷的，就沒辦法找最小出來
# 如果要偷的(stolen)比 k 小就代表還需要多偷一點，要把標準(mid)拉高一點點，所以下限就往上提到 mid
# 最終就可以找出要偷的閾值在哪裡了

# === Code ===
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        max_reward, min_reward = max(nums), 1
        houses = len(nums)
        
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            stolen = 0

            idx = 0
            while idx < houses:
                if nums[idx] <= mid_reward:
                    stolen += 1
                    idx += 2
                else:
                    idx += 1
            
            if stolen >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1
        
        return min_reward
