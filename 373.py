# 這題會給兩個遞增的 list，然後找出前 k 個數字和最小的組合
# 做法就是用 heap 配合上 set 來做，heap 先把數字組合拿出來家道結果裡面，然後確認兩個 list 各加一之後的組合有沒有遇過(有沒有在visit裡)，有較跳過沒就加進heap等處理

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        res = []
        m, n, visited = len(nums1), len(nums2), set()
        if not m or not n:
            return []
        h = [(nums1[0]+nums2[0], (0, 0))]

        for _ in range(min(k, m * n)):
            val, (i, j) = heappop(h)
            res.append([nums1[i], nums2[j]])
            if i + 1 < m and (i + 1, j) not in visited:
                heappush(h, (nums1[i + 1] + nums2[j], (i + 1, j) ) )
                visited.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in visited:
                heappush(h, (nums1[i] + nums2[j + 1], (i, j + 1) ) )
                visited.add((i, j + 1))
        return res
