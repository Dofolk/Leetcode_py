# 這題是給一個需要出差的日子是哪些天(1~365)，然後給一個costs代表1、7、30天的交通費價格
# 問怎樣的月票購買方式可以最便宜完成出差
# 這題的想法 DP，去紀錄前面日子的最低花費，然後要出差的時候就往前去計算怎麼買處理交通費最便宜
# 這邊的操作可以透過一個 point 來指向目前要處理的出差是哪天，如果不用出差直接把前一天的花費帶過來就好
# 遇到要出差的就去看看 1天的


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        point = 0
        M = max(days)
        dp = [0] * (M + 1)
        for idx in range(1, M + 1):
            if idx != days[point]:
                dp[idx] = dp[idx - 1]
                continue
            m1, m2, m3 = dp[idx - 1] + costs[0], float('inf'), float('inf')
            if idx >= 7:
                m2 = dp[idx - 7] + costs[1]
            else:
                m2 = dp[0] + costs[1]
            if idx >= 30:
                m3 = dp[idx - 30] + costs[2]
            else:
                m3 = dp[0] + costs[2]
            dp[idx] = min(m1, m2, m3)
            point += 1
        return dp[-1]
