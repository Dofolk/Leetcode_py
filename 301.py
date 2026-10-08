# ===== Question =====
# 題目給一個含有 () 以及英文字母的字串，移除掉一些(可以不移除)括號可以讓整個字串是合法的
# 問經過最少移除後合法的括號組合字串有哪些，回傳這些字串們(不限定順序)

# ===== Thoughts =====
# 這題就是要移除一些不合法的括號，讓字串合法，但如果是以 stack 的想法來做的話會少掉一些 case
# 例如 ()())XXXX 可以變成 ()()xxxx 或是(())xxxx，如果是 stack 就很可能只會剩 ()()xxxx
# 所以每一個可移除的選項都是一個分支 => 考慮 BFS 的操作來找到所有可能性，同時結合 DFS 快速針對每個 case 做深入探索
# 這邊就是一個一個位置開始走，然後遇到 ) 比較多的時候(位置在 idx)就開始清算，從我要找的片段往後到 idx 有多少可能性可以抽掉
# 以上面的例子來說就是當我走到 idx = 4 的 ) 時，我可以把前面的片段拆成 ()()xxxx 跟 (())xxxx 再往下去操作
# 這邊在往下操作(把可能加進BFS stack)時就只需要把拆分好的片段放下去，並且從相對應的 idx 跟 jdx 開始操作
# 刪除位置 jdx 一定在 idx 或它前面，所以刪掉後，原本 idx + 1 的字元會左移到 idx。 因此下一次從 idx 繼續掃，剛好接到還沒檢查的部分
# 而 jdx 也沿用，因為每個片段都只有掃到 jdx 就先刪除了，根本還沒往後看更多可以刪除的地方
# 這邊 BFS 的操作裡面還會透過一個 par 來記錄說現在要做的是找的是多餘的 ( 還是 )
# 另一個想法就是掃描兩次，我先從頭到尾把多餘出來的 ) 給剃除，並且把過程中有機會變成合法的候選人開一條新分支，拿去做反向掃描
# 反向掃描就是把每個分支不合法的 ( 從尾端往前掃出來後剔除，這樣兩遍掃描之後就可以得到每個組合都是合法的，而且移除的最少
# 因為我單向掃描就是做到單向的移除最少非法組合的部分

# Method 1 - Basic BFS Structure
class Solution:  # Iterative
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        stack = [(s, 0, 0, ("(", ")"))]

        while stack:
            cur, li, lj, par = stack.pop()
            n = len(cur)
            bal = 0
            match = False

            for i in range(li, n):
                bal += (cur[i] == par[0]) - (cur[i] == par[1])
                if bal >= 0:
                    continue

                for j in range(lj, i + 1):
                    if cur[j] == par[1] and (j == lj or cur[j - 1] != par[1]):
                        nxt = cur[:j] + cur[j + 1 :]
                        stack.append((nxt, i, j, par))

                match = True
                break

            if not match:
                rev = cur[::-1]

                if par[0] == "(":
                    stack.append((rev, 0, 0, (")", "(")))
                else:
                    res.append(rev)

        return res

# Method 2 - Forward and Backward 2 Pass
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []
        self.forward(s, res, 0, 0)
        return res
    
    def forward(self, s, res, left_idx, left_jdx):
        count = 0
        
        for idx in range(left_idx, len(s)):
            count += (s[idx] == '(') - (s[idx] == ')')
            if count >= 0:
                continue
            
            for jdx in range(left_jdx, idx + 1):
                if s[jdx] == ')' and (jdx == left_jdx or s[jdx - 1] != ')'):
                    next_s = s[:jdx] + s[jdx + 1:]
                    self.forward(next_s, res, idx, jdx)
            
            return
        
        self.backward(s, res, len(s) - 1, len(s) - 1)
    
    def backward(self, s, res, right_idx, right_jdx):
        count = 0

        for idx in range(right_idx, -1, -1):
            count += (s[idx] == ')') - (s[idx] == '(')
            if count >= 0:
                continue
        
            for jdx in range(right_jdx, idx - 1, -1):
                if s[jdx] == '(' and (jdx == right_jdx or s[jdx + 1] != '('):
                    next_s = s[:jdx] + s[jdx + 1:]
                    self.backward(next_s, res, idx - 1, jdx - 1)
        
            return

        res.append(s)
