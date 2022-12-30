# 這題是給一串計算是，然後找出所有可能的計算值(隨意加括號)
# 做法就是做 dfs，把一串數字作分割之後分別去計算可能性，然後再存好回傳就可以了

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        storage = {}
        def recurse(s, storage):
            if s in storage:
                print("here")
                return storage[s]
            ret = []
            for i in range(0, len(s)):
               
                if s[i] == "+":
                    first = recurse(s[:i], storage)
                    second = recurse(s[i + 1:], storage)
                    for f in first:
                        for sec in second:
                            ret.append(f + sec)
                elif s[i] == "-":
                    first = recurse(s[:i], storage)
                    second = recurse(s[i + 1:], storage)
                    for f in first:
                        for sec in second:
                            ret.append(f - sec)
                elif s[i] == "*":
                    first = recurse(s[:i], storage)
                    second = recurse(s[i + 1:], storage)
                    for f in first:
                        for sec in second:
                            ret.append(f * sec)
            if not ret:
                ret.append(int(s))
            storage[s] = ret
            return storage[s]
        return recurse(expression, storage)
