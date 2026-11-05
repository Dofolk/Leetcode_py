# ===== Question =====
# 給定兩個整數陣列 arr1、arr2 和整數 d，計算 arr1 中有多少個元素，與 arr2 的每個元素之差的絕對值都大於 d。
# 只要某個元素與 arr2 中任一元素的距離小於或等於 d，就不能計入。

# ===== Thoughts =====
# 這題可以直接做計算就好(method 1)，先把 arr2 做成 set 以便快速搜尋
# 然後每個 arr1 的值找範圍 d 裡面有沒有出現就好
# 另一種做法就是 bucket，把 arr2 的數值分進每個寬度 d + 1 的水桶(區間)裡
# 也就是說用 arr2 作區間出來(like method1 的 set，快速查詢用)
# 並記錄每個水桶的最高跟最低數值，接著去對 arr1 的值要先不在任何一個已知的區間內
# 因為在區間內的話 d + 1 的寬度強迫一定會撞到 arr2 的值
# 然後再確認往前一個區間的最大值跟往後一個區間的最小值不會撞到 arr1 的值，這樣就可以了

# Method 1 - Directly check
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        hashmap = set(arr2)

        ans = 0
        for num in arr1:
            check = True
            for v in range(num - d, num + d + 1):
                if v in hashmap:
                    check = False
                    break
            ans += check
        
        return ans

# Method 2 - Bucket check
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        width = d + 1
        low, high = dict(), dict()

        for v2 in arr2:
            bucket = v2 // width
            low[bucket] = min(low.get(bucket, v2), v2)
            high[bucket] = max(high.get(bucket, v2), v2)
        
        def check_dist(v):
            bucket = v // width
            return (
                bucket not in low and # 也可以 not in high
                high.get(bucket - 1, -inf) < v - d and
                low.get(bucket + 1, inf) > v + d
            )
        
        return sum(map(check_dist, arr1))
