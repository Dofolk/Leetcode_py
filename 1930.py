# 這題是給一個字串，然後要去找有幾個不重複的 3文字長的回文子字串，子字串可以不連續
# 做法就是以字元為出發點(26個)，先定位出文字最一開始跟最後出現的位置
# 然後再依據定位從中去找出有幾個不重複的回文子字串，也就是要找裡面有幾個不重複的文字就好了


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(set(s)) == 1:
            return 1
        D = defaultdict(list)
        C = defaultdict(int)
        for idx in range(len(s)):
            D[s[idx]].append(idx)
            C[s[idx]] += 1
        ans = 0
        for char in D:
            if C[char] == 1:
                continue
            for mid in D:
                if mid in s[ D[char][0] + 1: D[char][-1]] :
                    ans += 1
        return ans

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        Set = set(s)
        if len(Set) == 1:
            return 1
        
        ans = 0
        for char in Set:
            left, right = s.find(char), s.rfind(char)
            if left == right:
                continue
            seen = set()
            for mid_char in s[left + 1: right]:
                if mid_char in seen:
                    continue
                ans += 1
                seen.add(mid_char)
                if len(seen) == 26:
                    break
        return ans
