# 這題是給一個只有 0 跟 1 的字串，然後切成兩段，左邊計算 0 的數量，右邊則是計算 1 的數量
# 問整個字串依照這樣的計算方式，怎樣的切法可以拿到最大的總和
# 做法就是可以用 prefix sum 的概念來操作，先紀錄右邊總共幾個 1，然後再從左到右跑一遍
# 遇到 0 就紀錄左邊加一，並且把右邊紀錄 -1，然後再更新最大值就好了
# 另一種 prefix sum 的做法就是做每個位置往前的1數量，用 list 記錄起來
# 然後跑一遍字串來計算當下往前有幾個 0 (當下位置去減前面1的數量也就是prefix sum)跟最後一個位置到當下位置之間有幾個 1 (直接減就好)
# 最後更新最大值就好了


class Solution:
    def maxScore(self, s: str) -> int:
        left, right, M = 0, 0, 0
        L = len(s)
        for idx in range(L):
            right += 0 if s[idx] == '0' else 1
        for idx in range(L - 1):
            left += 1 if s[idx] == '0' else 0
            right += 0 if s[idx] == '0' else -1
            M = max(M, left + right)
        return M

class Solution:
    def maxScore(self, s: str) -> int:
        L = len(s)
        prefix = [int(s[0])]
        for idx in range(1, L):
            prefix.append(int(s[idx])+prefix[-1])
        M = 0
        for pos in range(0, L- 1):
            M = max(M, pos - prefix[pos] + 1 + prefix[L-1] - prefix[pos])
        return M
