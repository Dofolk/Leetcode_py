=== Question ===
# 題目是給一個 edges 的 (點1, 點2, 邊權重) list，還有最大數字 n 以及起終點列表 query
# 路徑走過所需的花費是當下路徑以及前面所有走過路徑的 AND(&) 值，問說在每個 query 最小花多少，如果沒有路徑就當成 -1

=== Thought ===
# 想要用 AND 找最小的話就是能多 AND 幾次就多 AND 下去，再加上題目沒有說不能重複走，所以其實是可以想成我能到的所有點都給他走過一遍
# 這樣就可以讓 AND 有最多的機會接觸所有可能的數字，降低 AND 出來的數字
# 因此，可以把題目想成是，我要去找所有端點怎麼分群，誰跟誰一群
# 這樣的話同一群的就可以知道說大家可以走那些條路，算出共同的結果，同時因為分群的原因也可以知道每個點最多能走的路徑 AND 值是多少
# 那分群的方法就是想到 union-find(可以參考readme)，透過union的時候順便紀錄所有可以走的路徑 AND 的值
# 最後對於 query 做 find 找共同群組回傳數值就好


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        edge_len, q_len = len(edges), len(query)
        if edge_len == 0:
            return [-1] * q_len
        boss = [idx for idx in range(n)]
        cost = [131071] * n
        rank = [1] * n

        def find(idx):
            if boss[idx] == idx:
                return idx
            return find(boss[idx])
        
        def union(u, v, w):
            u_final, v_final = find(u), find(v)
            if u_final != v_final:
                cost[u_final] &= cost[v_final] & w
                cost[v_final] = cost[u_final]
                if rank[u_final] >= rank[v_final]:
                    boss[v_final] = u_final
                    rank[u_final] += rank[v_final]
                else:
                    boss[u_final] = v_final
                    rank[v_final] += rank[u_final]
            else:
                cost[u_final] &= w
        
        for u, v, w in edges:
            union(u, v, w)
        ans = []
        for s, t in query:
            s_final, t_final = find(s), find(t)
            if s_final == t_final and cost[s_final] != 131071:
                ans.append(cost[s_final])
            else:
                ans.append(-1)
        return ans
