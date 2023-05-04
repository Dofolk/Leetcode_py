# 這題是給一個火柴棒長度的序列，然後看能不能拼成正方形
# 最一開始一定都是要去算四邊長然後去排除不合理的，接下來就是用 DFS 來找組合
# 需要輸入的有 目標長度(target), 用過的火柴(used), 有幾個邊要找(k), 比目標邊長還小的數字列表(colle), 從colle裡做組合的起始位置(start), 目前總和(S)
# 然後開始做 DFS 找組合，如果要找的邊只剩下一邊的話直接就是對的了，因為已經可以完成前面的邊長測試代表說邊長組合是沒問題的
# 接下來就確認從起始位置開始往後做 DFS 能不能找到解

class Solution:
    def makesquare(self, sticks: List[int]) -> bool:
        S = sum(sticks)
        if S % 4:
            return False
        edge = S >> 2
        colle = []
        for i in sticks:
            if i > edge:
                return False
            elif i < edge:
                colle.append(i)
        if len(colle) == 0:
            return True
        k = 4 - len(sticks) + len(colle)
        colle.sort(reverse = True)
        used = [False] * len(colle)

        def dfs(colle, used, start, target, S, k):
            if k == 1:
                return True
            
            i = start
            while i < len(colle):
                if not used[i]:
                    used[i] = True
                    if S + colle[i] < target and dfs(colle, used, i + 1, target, S + colle[i], k):
                        # 目前總和加上目前位置的值比目標小，而且從目前總和及下個位置往下尋找的時候是可以有解的時候
                        return True
                    if S + colle[i] == target and dfs(colle, used, 0, target, 0, k - 1):
                        # 目前總和剛好等於目標值，以及少了一個邊的向下尋找有解時
                        return True
                    used[i] = False
                    while i + 1 < len(colle) and colle[i + 1] == colle[i]:
                        # 調整下一步要做的位置，重複的值在前面的 if 裡面如果沒過的話代表說可以不用再重複做計算了
                        i += 1
                i += 1
            return False
        return dfs(colle, used, 0, edge, 0, k)
