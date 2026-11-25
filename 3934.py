# ===== Question =====
# 給定整數陣列 nums，找出最短的非空連續子陣列，使這串數字在 nums 中只出現一次，並回傳它的長度。
# 例如 nums = [1, 2, 1, 2]，1 和 2 都出現兩次，所以長度 1 不行。
# 長度 2 的 [1, 2] 出現兩次，但 [2, 1] 只出現一次，因此答案是 2。

# ===== Thoughts =====
# 這題直接左轉靈神

# Method - Binary Search + String Hash

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        naming = [nums]
        
        for b in range(n.bit_length() - 1):
            ids = {}
            curr_naming = []
            for pair in zip(naming[b], naming[b][2 ** b:]):
                curr_naming.append(ids.setdefault(pair, len(ids)))
            naming.append(curr_naming)
        
        def find(length):
            b = length.bit_length() - 1
            return 1 in Counter(zip(naming[b], naming[b][length - 2 ** b:])).values()
        
        return bisect_left(range(1, n), True, key = find) + 1

# Method 2 - ???

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        nxt, link, length = [{}], [-1], [0]
        last = 0

        for x in nums:
            cur = len(nxt)
            nxt.append({})
            link.append(0)
            length.append(length[last] + 1)

            p = last
            while p >= 0 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]

            if p >= 0:
                q = nxt[p][x]

                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(nxt)
                    nxt.append(nxt[q].copy())
                    link.append(link[q])
                    length.append(length[p] + 1)

                    while p >= 0 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]

                    link[q] = link[cur] = clone

            last = cur

        leaf = [True] * len(nxt)

        for v in range(1, len(nxt)):
            leaf[link[v]] = False

        return min(
            length[link[v]] + 1
            for v in range(1, len(nxt))
            if leaf[v]
        )
