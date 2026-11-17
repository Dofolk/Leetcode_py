# ===== Question =====
# 給定字串 s 和整數 k，將 s 切成恰好 k 個連續子字串，每段至少 2 個字元。
# 每段都要成為「半回文」：存在小於段長且能整除段長的正整數 d，使該段內索引除以 d 餘數相同的字元，依序組成的每一組都是回文。
# 每次可以將一個字元改成任意字母，求讓所有段都符合條件的最少修改總次數。

# ===== Thoughts =====
# 這題直接轉去找靈神，倒了，題目不是很好懂

# Method 1 - Recursion
divisors = [[] for _ in range(201)]
for d in range(1, 201):
    for multi in range(2 * d, 201, d):
        divisors[multi].append(d)

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def count_changes(start, end, d):
            if end - start <= d:
                return 0
            
            changes = 0
            right_start = end - d

            for pos in range(d):
                if s[start + pos] != s[right_start + pos]:
                    changes += 1
            
            return changes + count_changes(start + d, end - d, d)
        
        @cache
        def substring_cost(start, end):
            L = end - start
            min_cost = inf
            
            for d in divisors[L]:
                changes = count_changes(start, end, d)
                min_cost = min(min_cost, changes)
            
            return min_cost
        
        # DP
        best = {0: 0}
        
        for piece in range(1, k):
            room = range(2 * piece, n - 2 * (k - piece) + 1)
            new_best = {}

            for i in best:
                for j in room:
                    if i <= j - 2:
                        total_cost = best[i] + substring_cost(i, j)

                        new_best[j] = min(
                            new_best.get(j, inf),
                            total_cost
                        )
            best = new_best
        
        return min(best[i] + substring_cost(i, n) for i in best)

# Method 2 - By 灵茶山艾府
MX = 201
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i * 2, MX, i):
        divisors[j].append(i)

def get_modify(s: str) -> int:
    res = n = len(s)
    for d in divisors[n]:
        cnt = 0
        for i0 in range(d):
            i, j = i0, n - d + i0
            while i < j:
                cnt += s[i] != s[j]
                i += d
                j -= d
        res = min(res, cnt)
    return res

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        modify = [[0] * n for _ in range(n - 1)]
        for left in range(n - 1):
            for right in range(left + 1, n):  # 半回文串长度至少为 2
                modify[left][right] = get_modify(s[left: right + 1])

        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return modify[0][j]
            return min(dfs(i - 1, L - 1) + modify[L][j] for L in range(i * 2, j))
        return dfs(k - 1, n - 1)
