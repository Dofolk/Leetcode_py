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
