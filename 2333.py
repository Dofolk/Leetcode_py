# ===== Question =====
# 題目給兩個數字 list nums1 nums2，還有兩個數字 k1, k2
# 現在 nums1/nums2 可以對於任意位置的 element 進行 k1/k2 次的 +1 or -1 操作
# 求出對於每個 idx， (nums1[idx] - nums2[idx]) ^ 2 的最小總和是多少

# ===== Thoughts =====
# 這題就是要算兩個對應位置的數字差的平方總和，然後要做有限操作下的數值最小化
# 所以核心的概念就是算出全部數字差有多少，然後找出一個能在限定操作下最小化的數值
# 所以這邊就是盡可能壓低大的數值，因為這樣才可以讓整體的總和下降最快
# 下降快的原因是 m^2 - (m-1)^2 = 2m - 1，所以當 m 越大的時候下降的收益越大
# 另外可以留意一下， k1 k2 可以核算，因為你只要把對應位置的差距縮小就好
# 如果其中一個操作次數耗盡，只需要對於另一個做反向操作就好，像是 nums1[idx] + 1 就是 nums2[idx] - 1
# 最後，整個流程就是，先找出數字差後去確認現有操作次數能不能壓到 0
# 然後就對於每個數字差作數量統計，接著開始計算把最高的數字削平成次高數字需要多少操作次數
# 如果削平花費次數沒有超過現有的次數就把現有次數扣掉之後進行下一輪的削平
# 如果會超過，就開始計算手頭上 diff_count 個數字平均往下砍能砍多少掉
# 像是手頭上已經把 10 個位置的數字砍到 18 了，次高是10，但只剩下 23 次，算起來可以把 10 個 18 坎城 10 個16
# 再把手上剩下的三次挑其中三個砍就可以了
# 所以就去計算權不能齊頭削平(full)，再算算餘下的次數(extra)，最後把答案組合起來就可以了

# Method 1 - 削平法
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        total = sum(diff)
        mod_time = k1 + k2
        if total <= mod_time:
            return 0
        
        diff = sorted(Counter(diff).items(), reverse = True)
        diff.append((0, 0))

        # 當需要把高度往下削的時候，用 diff_count 來記錄目前手頭上總共有多少個位置需要一起削
        diff_count = 0

        for d in range(len(diff)):
            height, count = diff[d]
            next_height = diff[d + 1][0]
            
            diff_count += count
            gap = height - next_height
            k_cost = gap * diff_count

            if mod_time >= k_cost:
                mod_time -= k_cost
            else:
                full_dropout = mod_time // diff_count
                extra_dropout = mod_time % diff_count
                new_height = height - full_dropout

                res = (
                    (diff_count - extra_dropout) * new_height ** 2
                    + extra_dropout * (new_height - 1) ** 2
                )
                
                for h, c in diff[d + 1:]:
                    res += c * h ** 2
                break
        
        return res


# Method 2 - Binary Search the Target Level
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        total = sum(diff)
        mod_time = k1 + k2
        if total <= mod_time:
            return 0
        
        diff = Counter(diff)
        
        M, m = max(diff.keys()), (total - mod_time) // len(nums1)

        # Binary Search the Suitable Level
        while m < M:
            mid = (M + m) // 2
            count = 0
            for key, value in diff.items():
                if key > mid:
                    count += (key - mid) * value
                    if count > mod_time:
                        break
            if count > mod_time:
                m = mid + 1
            else:
                M = mid

        ans = 0
        for key, times in diff.items():
            if key < m:
                ans += (key ** 2) * times
            else:
                ans += (m ** 2) * times
                mod_time -= (key - m) * times
        
        return ans - (m * 2 - 1) * mod_time
