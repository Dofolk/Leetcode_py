# 這題是給一串字串，然後要移除重複的部分，並且把結果做成 smallest in lexicographical order 回傳
# 做法就是先找一下每個字母最後一個字在哪裡，然後再去做調整
# https://leetcode.com/problems/remove-duplicate-letters/solutions/1859515/python-o-n-beats-98-stack-detailed-explanation-simple/?orderBy=most_votes

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_pos = {}
        stack = []
        visited = set()
        
        for i in range(len(s)):
            last_pos[s[i]] = i

        for i in range(len(s)):
            if s[i] not in visited:
                while stack and stack[-1] > s[i] and last_pos[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        
        return ''.join(stack)
