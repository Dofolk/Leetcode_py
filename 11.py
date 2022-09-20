# 這題就是要找水缸可以擁有的最大水量
# 用 two pointer來操作，從最旁邊開始往內找，一直更新最大值就可以了

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R, M = 0, len(height) - 1, 0
        while L<R:
            M = max(M, min(height[L],height[R])*(R-L) )
            if height[L]<height[R]:
                L += 1
            else:
                R -= 1
        return M
