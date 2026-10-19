# ===== Question =====
# 題目會給一個常數 list，然後把數字做分群及排序，分群方式是先以各個位數總和做小到大排序
# 每個群內在依據數字做小到大排序，得到最終排序後的成果
# 問說原本的 nums 變成最終排序結果，最少需要多少次的元素交換

# ===== Thoughts =====
# 這邊就是先把最終結果給找出來，然後把每個數字最終該在的位置給找出來(pos)
# 然後可以用簡單的利子去找看看規律或是操作方法，像是 2341 -> 3241 -> 4231 -> 1234
# 如果把排序前後的位置做對應可以看到 idx 0 -> idx 1 -> idx 2 -> idx 3 -> idx 0  這樣的 cyccle
# 所以這就可以看成是再找 cycle 的循環 -> 而每個 cycle 要做到好就給得要交換 len(cycle) - 1 次
# 最終這邊就是去找 cycle，用 visited 跟 pos 來記錄每個 cycle 要怎麼走怎麼做 permutation

# Method - Observation cycle permutation
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def DigitSum(val):
            s = 0
            while val:
                s += val % 10
                val //= 10
            return s
        
        n = len(nums)

        sort_list = sorted(
            [(DigitSum(num), num, idx) for idx, num in enumerate(nums)]
        )

        pos = [tp[2] for tp in sort_list]
        
        
        visited = [False] * n
        swap = 0

        for idx in range(n):
            if not visited[idx]:
                cycle_len = 0
                jdx = idx
                
                while not visited[jdx]:
                    visited[jdx] = True
                    jdx = pos[jdx]
                    cycle_len += 1
                swap += cycle_len - 1
        
        return swap
