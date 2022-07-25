from math import sqrt

class Solution:
    def climbStairs(self, n: int) -> int:
        alpha = (1-sqrt(5))/2
        beta = (1+sqrt(5))/2
        return int((pow(beta,n+1)-pow(alpha,n+1))/sqrt(5))
        
# Fabonacci
