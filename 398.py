# 這題是給一個 class 做定義，要隨機從符合目標值的 index 裡面隨機回傳一個
# 做法就是用 dict()，遇到有重複的就直接隨機回傳，沒有的話就先把整個 list 跑一遍之後新增進去跟回傳

class Solution:

    def __init__(self, nums: List[int]):
        self.num = nums
        self.d = defaultdict(list)

    def pick(self, target: int) -> int:
        if target in self.d:
            return random.choice(self.d[target])
        picklist = []
        for idx, num in enumerate(self.num):
            if num == target:
                picklist.append(idx)
        self.d[target] = picklist
        return random.choice(picklist)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
