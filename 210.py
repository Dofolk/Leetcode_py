# 這題跟207類似，一樣要找能不能好好修完課，會給修課堂數跟修課順序，如果可以好好修完課就輸出修課順序(優些課堂美給順序的話可以隨便放沒關係)，不行就回傳[]
# 做法跟207一樣，看看有沒有 cycle，沒有的話就可以把課堂放進去結果裡面，這樣每走一個連貫的順序時就可以順便存好了

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visit = [ 0 for _ in range(numCourses)]
        res = []
        for x, y in prerequisites:
            graph[x].append(y)
        
        def dfs(i):
            if visit[i] == -1: return False
            if visit[i] == 1: return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j): return False
            visit[i] = 1
            res.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return res
