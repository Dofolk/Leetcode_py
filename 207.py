# 這題是給一個數字表示說要修課的數量，然後再給一個 List 來表示說修課的前後順序，最後看這樣的修課順序合不合理以及能不能修完課
# 做法就是去找看看每堂課程當第一堂躍上的課時，往下去找會不會修到重覆的課(就是看看有沒有cycle)
# 所以就用一個 graph 來存上課的順序點，然後一個陣列存有沒有走過，確保不會有迴圈出現

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for _ in range(numCourses)]
        visit = [ 0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        
        def dfs(i: int) -> bool:
            if visit[i] == -1: return False
            if visit[i] == 1: return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j): return False
            visit[i] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
