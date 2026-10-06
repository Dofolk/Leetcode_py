# ===== Question =====
# 題目給兩個只有 0 1 的 2d array img1 跟 img 2，然後經過平移兩個 image 去算兩個的重疊率，回答最高重疊多少
# 在移動的時候只會有水平移動跟垂直移動，不會有旋轉

# ===== Thoughts =====
# 這題可以去想說如果我兩個 image 的 1 做全映射，然後把每個映射過程需要移動的步數給記起來
# 那我就可以知道說怎樣的走法(水平移動多少，垂直移動多少)可以獲得最好的結果
# 所以這邊就先把各自 1 的位置給記錄起來，然後用一個 double for loop 來計算全映射
# 每個都對應到的時候會需要走 dx dy 步，用 count 紀錄有幾個 1 走這樣的步數可以對應到另一個 image 的 1
# 最後再隨時更新最佳結果就可以了
# 這題還有另一個想法，就是這題在找兩個 image 的 cross correlation
# cross-correlation 可以透過 flip 其中一張 image 轉成 convolution
# 直接計算時，大約是 n^2 個 shift * 每次 n^2 個 pixel => O(n^4)
# 接著套用 convolution theorem，用 Fourier Transform 加速 convolution
# F(f * g) = F(f) · F(g)，其中 * 是 convolution，F 是 Fourier Transform
# 最後再做 inverse Fourier Transform，就能得到 convolution / correlation 的結果

# Method1 - Injective whole 1
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = [(idx, jdx) for idx in range(n) for jdx in range(n) if img1[idx][jdx] == 1]
        B = [(idx, jdx) for idx in range(n) for jdx in range(n) if img2[idx][jdx] == 1]

        count = [ [0] * (2 * n) for _ in range(2 * n)]
        best = 0

        for xa, ya in A:
            for xb, yb in B:
                dx = xb - xa + n
                dy = yb - ya + n
                count[dx][dy] += 1
                best = max(best, count[dx][dy])
        
        return best

# Method2 - Cross correlation
import numpy as np

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a = np.array(img1, dtype=np.int8)
        b = np.array(img2, dtype=np.int8)
        b = np.flip(b)

        n = len(img1)
        shape = (n * 2 - 1, n * 2 - 1)
        fa = np.fft.fft2(a, shape)
        fb = np.fft.fft2(b, shape)
        c = np.rint(np.fft.ifft2(fa * fb).real)

        return int(c.max())
