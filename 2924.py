# 這題是有 n 個隊伍，然後給一個 DAG(directed acyclic graph, 有向無環圖) 來代表每個隊伍之間的強弱，點為隊伍編號，邊 (a, b) 為 a 隊伍比 b 隊伍強，問能不能找到唯一的最強隊伍
# 這題的想法很簡單，就是先給點，這個意思就是最一開始還沒有強弱之分的時候大家都可以是最強的，所以先宣告 n 個 True 代表每隊都是最強的
# 等到強弱之分加進來之後，開始從頭到尾跑 edges，將弱於人的隊伍剃除改成 False
# 最後就看看剩幾個 True 就可以知道有沒有唯一最強的了

# method 1 beats 49%
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # use set to record teams that stronger than others
        strong_team = set(range(n))
        # one for loop to remove weaker teams
        for _, weak in edges:
            if weak in strong_team: # high time cost
                strong_team.remove(weak)
        if len(strong_team) == 1:
            return strong_team.pop()
        return -1

# method 2 beats 100%
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # use list to record teams that stronger than others
        # initial it as at first everyone is the strongest
        win_team = [True] * n
        for _, w in edges:
            # set weaker teams as False
            win_team[w] = False
        return win_team.index(True) if win_team.count(True) == 1 else -1
