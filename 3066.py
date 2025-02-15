# 這題是給一個數字 list 跟一個數字 k，每次從 list 裡面推出最小的兩個數字，然後把小的 *2 之後再加上大的那個，再推回去 list 裡面
# 重複這樣的操作，需要做幾次才可以把 list 裡面的數字都弄得 >= k
# 做法就是用 heap 來取數字，取數字之後就做 *2 跟相加，接著用 heappushpop() 來把當下的數字跟 heap 裡面最小的數字做交換
# 在記錄操作的步數，最後回傳總步數就好了

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        val = heapq.heappop(nums)
        while val < k:
            add_res = val * 2 + heapq.heappop(nums)
            val = heapq.heappushpop(nums, add_res)
            count += 1
        return count
