


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
