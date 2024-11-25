# 這題是給一個固定 2 x 3 的陣列，然後裡面數字就是 0 ~ 5，每次都可以將相鄰的兩個數字做交換，問最少能幾步將整個陣列換成 123450 (左上->右下)，如果不能的話就回傳 -1
# 這題就是用 BFS 去找路徑，因為 BFS 的操作是 FIFO，所以這邊用 deque() 的話速度會快上很多，接下來就是把操作變得比較簡單
# 把陣列壓平成一個字串，這樣在做比較的時候方便，然後是還需要一個 set 紀錄走過的有哪些，還有需要說每個位置他走的地方步一樣，所以用一個 dir 來記錄說下一步能走去哪裡
# 接著就是做 BFS，先把上一輪存進 queue 裡面的結果都拿出來，然後對於每個結果都檢查是不是目標，是的話就可以回傳了
# 不是的話就開始看看這一輪所有狀態的下一步可能是什麼，在只移動 0 的狀況下把所有沒走過的可能狀態再丟回去 queue 裡面等待下一輪的檢查
# 重複將 queue 裡面的東西丟出來再放回去，直到走遍所以可能或遇到目標，就可以回傳 step 或是 -1 了

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # every position has its own direction for one step
        dir = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        target = "123450"
        visited = set()
        q = deque()
        # flatten the matrix into 1-dimension string
        start = ''.join(str(v) for v in board[0]+board[1])
        
        q.append(start)
        visited.add(start)
        step = 0

        while q:
            size = len(q)
            # use for loop to run all possible states in this turn and then handle all the possible state of the next turn after for loop
            for _ in range(size):
                current = q.popleft()
                if current == target:
                    return step
                
                zero_pos = current.index('0')
                for move in dir[zero_pos]:
                    next_state = list(current)
                    next_state[zero_pos], next_state[move] = next_state[move], next_state[zero_pos]
                    next_state = ''.join(next_state)
                    if next_state not in visited:
                        visited.add(next_state)
                        q.append(next_state)
            step += 1
        return -1
