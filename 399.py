# 這題是給一些字母的倍數關係，然後去找出所求得字母倍數關係
# 做法是把所有的字母組合作成圖，然後再去更新倍率

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(graph, start, end, visited):
            if start == end and graph[start]:
                return 1.0
            
            visited.add(start)
            for neigh, val in graph[start]:
                if neigh in visited:
                    continue
                tmp = dfs(graph, neigh, end, visited)
                if tmp > 0:
                    return val * tmp
            
            return -1.0

        graph = defaultdict(set)
        for items, val in zip(equations, values):
            x, y = items
            graph[x].add((y, val))
            graph[y].add((x, 1.0/val))
        
        res = []
        for q in queries:
            res.append(dfs(graph, q[0], q[1], set()))
        
        return res
