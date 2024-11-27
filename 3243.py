# 這題是說給 n 個點，按照順序每個點都可以跟後一點連接，然後現在給捷徑，從 i 點可以直接到 j 點，試問每次給捷徑之後，最少走多少步可以到最後一點
# 想法就是有給捷徑就去判斷要不要做步數的 bfs 更新，先把每個點最少能走到的步數記起來，然後用 dict 來記錄捷徑
# 接下來就是去確認這條捷徑加進來之後，目的地的最小步數會不會更小，會的話就 bfs 更新一下目的地點，不會比較小的話就代表這條捷徑不中用，已經有其他更好的路徑
# Note: 在 bfs 的時候可以多做一步確認，確認說我往下走的時候確實可以讓目的地點步數變小再把目的地點給加進去 queue 裡面，減少進去 queue 的東西來加速
# Note: 因為一般來說都會再開始 queue popleft 的時候就把下面幾步的目標全丟進去 queue 裡面，所以多一步篩選少做幾次無用功


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        link = defaultdict(list)
        for i in range(n - 1):
            link[i].append(i + 1)
        
        record = [i for i in range(n)]

        def bfs(pos):
            q = deque([pos])
            while q:
                pos = q.popleft()
                for v in link[pos]:
                        if record[v] > record[pos] + 1:
                            record[v] = record[pos] + 1
                            q.append(v)
        
        for i, j in queries:
            link[i].append(j)
            if record[j] > record[i] + 1:
                record[j] = record[i] + 1
                bfs(j)
            res.append(record[-1])
        return res
