


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
