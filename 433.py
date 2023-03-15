# 這題是在看基因序列從 start 到 end 要變換多少次，然後每次變換都要在給定的 bank 裡面有出現才可以
# 做法就是用 queue 來記錄要做的序列以及 seen 來記錄看過的序列

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        Q, seen = collections.deque([(start, 0)]), {start}
        while Q:
            s, n = Q.popleft()
            if s == end:
                return n
            for i in range(8):
                for ch in 'ACTG':
                    m = s[:i] + ch + s[i+1:]
                    if m in bank and m not in seen:
                        seen.add(m)
                        Q.append((m, n + 1))
        return -1
