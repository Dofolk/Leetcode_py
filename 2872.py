# 這題是給一個 edge 的 list，代表說 n 個點之間的連結，然後再給一個 values 來表示每個點的數值，然後對於給定的 k，如何讓給定的連結做出最多的子集合，並且讓子集合的 values 是 k 的倍數
# 也就是說是類似 tree 的結構，然後把連結切斷，每個切出來的子集合(子樹)都是 k 的倍數，然後把子集合數量切到最大
# 這題就是用 dfs 做處理，用深度找出最末端的子集合，來判斷能不能切開來做出子集合
# 首先做節點之間的關係，然後再 dfs 開始找數字總和，dfs 回傳 mod k 之後的總和
# dfs 裡面的節點就是先做自相鄰的點，如果不是母節點的話就可以做 dfs 的數值相加，相加之後做 mod k，接著就判斷一下能不能被 k 整除，能就加個次數

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        neighbor = [[] for _ in range(n)]
        for node1, node2 in edges:
            neighbor[node1].append(node2)
            neighbor[node2].append(node1)
        count = [0]

        def dfs(current_node, parent_node, neighbor, values, k, count):
            total_sum = 0
            
            for neighbor_node in neighbor[current_node]:
                if neighbor_node != parent_node:
                    total_sum += dfs(neighbor_node, current_node, neighbor, values, k, count)
                    total_sum %= k
            total_sum += values[current_node]
            total_sum %= k
            
            if total_sum == 0:
                count[0] += 1
            return total_sum
        
        dfs(0, -1, neighbor, values, k, count)
        return count[0]
