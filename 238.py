# 這題是給一個 list，然後在對應位置 (i-th) 的地方回傳除了 i-th 之外所有值的乘積
# 做法就是 list 往左往右通通跑一遍(現在的 list 分成3部分: i-th點，頭到i-1，i+1到尾
  # 由左向右跑的時候就是把 i-th 前的所有項都乘一遍(完成 頭到i-1 的乘積並儲存在第 i 格輸出位)
  # 由右往左跑的時候就是反方向把 i+1到尾 的這段都乘起來(完成 i+1到尾 的乘積並儲存在第 i 格輸出位)
# 可以想成雙方向的乘積累積

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prod = 1
        for i in range(1,n):
            prod *= nums[i-1]
            res[i] *= prod
        prod = 1
        for i in range(n-2, -1, -1):
            prod *= nums[i+1]
            res[i] *= prod
        return res
