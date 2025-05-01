# === Description ===
# 題目給工作能力負擔表 workers，任務負擔表 tasks，強化藥劑數量 pills 跟強化效果 strength
# 每個人只能做自身能力負擔或是負擔以下的任務，問給定的能力及任務，最多可以做幾個任務
#
# === Thought ===
# 首先對工作能力及任務作排序，然後用 binary search 來找看看 k 個任務能不能負擔的起
# 可以就提升任務數量(移動 left)，不能負擔就降低數量(移動 right)
# 在考慮能否負擔就是貪婪算法的概念去做，先是看最硬的任務及最有能力的人能不能對上，能就直接讓他把任務給吃了
# 不能就是看看有沒有前面保存起來的人力或是強化之後能不能吃掉任務
# 如果強化之後可以有很多人可以吃掉的話，就讓原始能力最低的吃，這樣可以讓強化藥劑獲得最大效益
# 最後回傳 k 個任務能不能吃得下來
#
# === Code ===

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort(reverse = True)
        
        def afford(k, p = pills):
            worker = 0
            q = deque() #當下任務用強化藥劑之後能扛任務的有幾個
            for task in range(k - 1, -1 ,-1):
                if len(q) == 0 and workers[worker] >= tasks[task]: #原始能力已足夠的，就直接吃下任務
                    worker += 1
                    continue
                if len(q) > 0 and q[0] >= tasks[task]: #看看前面被保留的人有哪些
                    q.popleft()
                    continue
                while worker < k and workers[worker] + strength >= tasks[task]: #強化之後能扛當下任務的有誰
                    q.append(workers[worker])
                    worker += 1
                if len(q) > 0 and p > 0: #讓原始能力最低的吃強化藥劑扛任務，讓強化藥劑收益最大化，僅限於有人也還有剩的強化藥劑才能做
                    q.pop() #踢掉原始能力最低的去吃藥
                    p -= 1 #因為要吃藥所以扣掉一罐藥劑
                    continue
                return False
            return True
        
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = left + right + 1 >> 1
            if afford(mid):
                left = mid
            else:
                right = mid - 1
        return left

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def afford(k, p = pills):
            worker = workers[-k:]
            for task in tasks[:k][::-1]:
                if task <= worker[-1]: #能的話直接吃下來
                    worker.pop()
                elif p and task <= worker[-1] + strength:
                    p -= 1
                    idx = bisect.bisect_left(worker, task - strength) #最大化強化藥劑的效果
                    worker.pop(idx)
                else:
                    return False
            return True
        
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = left + right + 1 >> 1
            if afford(mid):
                left = mid
            else:
                right = mid - 1
        return left
