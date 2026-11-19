# ===== Question =====
# 給定一個整數陣列 nums，可以任意修改其中最多兩個元素的值。
# 陣列的分數（Score）定義為最大值與最小值的差，即 max(nums) - min(nums)。
# 請找出修改最多兩個元素後，能得到的最小分數。

# ===== Thoughts =====
# 這題是要最小化總和，因為可以任意更改兩個數字，所以最小值的部分可以不去考慮
# 最小值不需要考慮的原因是在兩次更改中可以把育更改的數字改成任一個重複的數字就可以達成 0 了
# 接下來就是去考慮如何把最大值給降下來，最大值來源就是最大數減去最小數
# 因為可以修改兩次，所以我們要考慮三種組合，最小三個跟最大三個
# 考慮他們之間的關係就可以了，改掉的選擇就是: 最大兩個數、最小兩個數或是最大最小各一

"""
diff1, diff2, diff3 = v3 - v1, v2 - v1 + u3 - u2, u3 - u1
M = max(diff1, diff2, diff3)
if diff3 == M:
    return u1 - v1
elif diff1 == M:
    return u3 - v3
else:
    return u2 - v2
"""

# Method 1 - Sort
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3 or len(set(nums)) == 1:
            return 0
        
        nums.sort()

        v1, v2, v3 = nums[0], nums[1], nums[2]
        u1, u2, u3 = nums[n - 3], nums[n - 2], nums[n - 1]

        return min(u3 - v3, u2 - v2, u1 - v1)

# Method 2 - Python Heap function
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3 or len(set(nums)) == 1:
            return 0
        
        min1, min2, min3 = heapq.nsmallest(3, nums)
        max1, max2, max3 = heapq.nlargest(3, nums)
        return min(max3 - min1, max2 - min2, max1 - min3)
