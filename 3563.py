
'''
這個方法是使用差分陣列+modulo的概念來實作的，同時透過費馬小定理來加速運算
如果沒有用這個方法的話也可以直接暴力解(brute force)，在數量級不大的狀況下也是可以過得
'''
from collections import defaultdict
from typing import List

# 主要的想法就是透過 mod 的概念來把原本步幅k產生的跳點式update變成連續式的update
# 因為取 mod 之後就直接變成k的n_i倍，那這樣的話就可以變成是連續的了，像是k 的 2,3,4倍對應到 2*k + rem = left
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        updates = defaultdict(lambda: defaultdict(list))

        # 根據步幅分門別類，同步幅同mod起點的就擺一起處理
        # start: 紀錄倍率，在步幅k且mod起點為rem的條件下，真正的起點是mod起點的多少倍步幅之遠
        # end意義同start
        for l, r, k, v in queries:
            rem = l % k
            start = (l - rem) // k
            end = (r - rem) // k
            updates[k][rem].append((start, end, v))

        mult = [1] * n

        # 來更新原始數據相對應的每個位置要乘的倍率是多少
        for k in updates:
            for rem in updates[k]:
                # 根據步幅及起點來決定 mod 後的差分陣列要開多大
                # diff: mod 步幅後的差分陣列
                size = (n - rem + k - 1) // k
                diff = [1] * (size + 1)

                # 針對對應位置先給他乘上 v，然後再結尾的地方除以 v
                # 把差分陣列的想法變成式乘法的，透過費馬小定理來做到更快的除法(prime - 2)
                for s, e, v in updates[k][rem]:
                    diff[s] = diff[s] * v % MOD
                    if e + 1 < len(diff):
                        diff[e + 1] = diff[e + 1] * pow(v, MOD - 2, MOD) % MOD

                # 開始累積差分(乘法)陣列的數值，用 cur 來做乘法累積
                # 同時間也一起把累積出來的數值回傳到mult這個原始數據的倍率上面
                cur = 1
                for i in range(size):
                    cur = cur * diff[i] % MOD
                    idx = rem + i * k
                    if idx < n:
                        mult[idx] = mult[idx] * cur % MOD

        # 算出每個位置應該乘多少之後就來更新原始數據
        for i in range(n):
            nums[i] = nums[i] * mult[i] % MOD

        # 更新完原始數據之後來算出XOR答案
        ans = 0
        for x in nums:
            ans ^= x

        return ans
