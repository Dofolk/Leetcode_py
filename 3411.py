# ===== Question =====
# 給你一個正整數陣列 nums，找出最長的連續子陣列
# 使其所有元素的乘積等於這些元素的最大公因數（GCD）乘以最小公倍數（LCM），並回傳該子陣列的長度。

# ===== Thoughts =====
# 這題直接正向想直接做也是沒有問題的，因為數量限制小所以直接 double for 遍歷一遍子陣列就好了
# 另一種方法就是反方向來想，在怎樣的狀況下 prod != gcd * lcm？質因數分解有重複質因數時就會不相等
# 所以針對每個數字的質因數做確認，檢查該質因數在前面的哪邊出現，就直接從該位置往後算長度

# Method 1 - Directly Search
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        def checker(arr):
            gcd_val = lcm_val = prod = arr[0]
            for num in arr[1:]:
                prod *= num
                gcd_val = math.gcd(gcd_val, num)
                lcm_val = math.lcm(lcm_val, num)
            return gcd_val * lcm_val == prod
        
        ans = 1
        for right in range(len(nums) - 1, 0, -1):
            for left in range(0, right):
                if right - left + 1 < ans:
                    continue
                curr_arr = nums[left:right + 1]
                if checker(curr_arr):
                    ans = max(ans, right - left + 1)
        
        return ans

# Method 2 - Prime checker
primes = (
    (),
    (),
    (2, ),
    (3, ),
    (2, ),
    (5, ),
    (2, 3),
    (7, ),
    (2, ),
    (3, ),
    (2, 5),
)

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        last_seen = [-1] * 8
        res = min(len(nums), 2)
        left = 0
        
        for right, num in enumerate(nums):
            for p in primes[num]:
                if last_seen[p] >= left:
                    left = last_seen[p] + 1
                last_seen[p] = right
            res = max(res, right - left + 1)
        
        return res
