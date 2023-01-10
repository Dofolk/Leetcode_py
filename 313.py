# 這題是給一個數字 n 跟 質數表，從質數表裡面去構成數字，意思就是當下能存活的數字只能是表中數字的乘積，找出地n個數字是多少
# 做法就是用heap，逐個把值丟出來乘做出整個表
# https://leetcode.com/problems/super-ugly-number/solutions/868948/python3-l-faster-than-99-35-using-heapq/

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        num = primes.copy()
        heapq.heapify(num)
        p = 1
        for i in range(n-1):
            p = heapq.heappop(num)
            for prime in primes:
                heapq.heappush(num, p * prime)
                if p % prime == 0:
                    break
        return p
