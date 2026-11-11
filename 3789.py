# ===== Question =====
# 有兩種需求，分別至少要滿足 need1 和 need2 個單位。
# 你可以花 cost1 或 cost2 單獨滿足對應需求的一個單位，也可以花 costBoth 同時滿足兩種需求各一個單位。
# 回傳滿足所有需求的最低總花費，允許購買超過需求的數量。

# ===== Thoughts =====
# 這題可以做最小化消耗，然後 costBoth 多大就會決定該如何選擇 need1 need2 該怎麼使用
# 所以考慮的是 cost1 cost2 跟 costBoth 的大小關係，並且對於每個區間段作相對應的處理(參考 method 2)
# 區間段: [題目 min, cost1], [cost1, cost2], [cost2, cost1 + cost2], [cost1 + cost2, 題目 max]

# Method 1 - Greedy
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        return (
            min(need1, need2) * min(costBoth, cost1 + cost2) +
            max(0, need1 - need2) * min(cost1, costBoth) +
            max(0, need2 - need1) * min(cost2, costBoth)
        )

# Method 2 - Greedy
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1 > cost2:
            cost1, cost2 = cost2, cost1
            need1, need2 = need2, need1
        
        # costBoth is larger than cost1 + cost2 and never use Both
        if costBoth >= cost1 + cost2:
            return cost1 * need1 + cost2 * need2
        # costBoth smaller than smallest cost and apply it for all need
        if costBoth <= cost1:
            return costBoth * max(need1, need2)
        # costBoth in interval cost1 and cost2, apply costBoth instead cost2
        # and add remaining need1 with cost1
        if costBoth <= cost2:
            return costBoth * need2 + cost1 * max(0, need1 - need2)
        # costBoth in interval cost2 and cost1 + cost2, apply costBoth with the overlap amount of need1 and need2
        # and add remaining need1, need2 with cost1, cost2 corresponding
        m = min(need1, need2)
        return costBoth * m + cost1 * max(0, need1 - m) + cost2 * max(0, need2 - m)
