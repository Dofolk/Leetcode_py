# 這題是給一個 2d array，代表每個班級考試的 [通過人數, 班上總人數]，然後現在有頂尖轉學生 extraStudents，他們必定通過考試
# 試問如何將這些頂尖學生加到班級內，可以提升所有班級的平均通過率，也就是所有班級通過率相加之後再除以總班級數
# 想法是每個班級如果加一個頂尖學生進來後可以提昇說多少通過率，透過通過率的高低作 heap 來加速搜尋與取用
# 當遇到增加通過率為 0 時直接回傳 1，代表都不用更新了，大家都好棒棒不會被當
# 不然就是開始對於 heap 做 pop，找可以提升最多的班級優先加入頂尖學生，接著更新通過率、通過人數及班級總人數，最後再將結果推回去 heap
# 作後回傳除完之後的結果加總就好

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes = [ ( p/c - (p + 1) / (c + 1), p, c) for p, c in classes]
        heapq.heapify(classes)
        if classes[0][0] == 0:
            return 1
        for _ in range(extraStudents):
            _, p, c = heapq.heappop(classes)
            heappush(classes, ( (p + 1) / (c + 1) - (p + 2) / (c + 2), p + 1, c + 1))
        return sum([p/c for _, p, c in classes])/len(classes)
