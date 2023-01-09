# 這題是給一堆指令，然後設計相對應的函數
# update 就是把特定位置的值改掉，然後sumrange就是把範圍內的和加起來送出去
# 這邊在初始化的時候宣告：s來存全部總和，l來存長度，c來存快取(cache)，n來存最一開始的 list
# 在 update 的時候就是把快取清空，調整總和跟相對應位置的值
# 在 sum 的時候就是先從快取找看看有沒有出現過，有的話就不用再算一次了，沒有的話就看長度多少，沒有過半的話直接 sum，有的話就用減的(total-左-右)
# 最後記得把快取多新增剛剛算的結果以方便下一次取用

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = nums    
        self.s = sum(nums)
        self.l = len(nums)
        self.c = {} # cache
     
    def update(self, index: int, val: int) -> None:
        self.c = {}
        self.s -= self.n[index]
        self.n[index] = val
        self.s += val
        

    def sumRange(self, left: int, right: int) -> int:
        if '{}_{}'.format(left, right) in self.c:
            return self.c['{}_{}'.format(left, right)]
        if right - left > self.l / 2:
            ans = self.s - sum(self.n[:left]) - sum(self.n[right + 1:])
        else:
            ans = sum(self.n[left:right + 1])
        self.c['{}_{}'.format(left, right)] = ans
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
