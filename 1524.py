# 這題

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_count, even_count, prefix = 0, 1, 0
        for val in arr:
            prefix += val
            if prefix % 2:
                odd_count += 1
            else:
                even_count += 1
        return (odd_count * even_count) % (10**9 + 7)
