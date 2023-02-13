# 這題是要做一個 class，要做洗牌的東西
# reset 就是要回歸原本的樣子，就不去動就好了
# 洗牌就直接做隨機交換就好

class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums[:]

    def reset(self) -> List[int]:
        return self.array

    def shuffle(self) -> List[int]:
        res = self.array[:]
        L = len(res)
        for i in range(L):
            idx = random.randrange(i, L)
            res[idx], res[i] = res[i], res[idx]
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
