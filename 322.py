# 這題是給硬幣面額跟目標金額，找最少幾個硬幣可以湊成目標
# 做法是用 BFS 找，需要有兩個 list 來存前一次的成果跟這一次的成果
# 從前一次的成果裡面每個都拿出來加上每個硬幣幣值，剛好的話就直接回傳數量就可以了，超過的話就跳過這次操作，因為在往下去加的話一樣是超過的沒意義
# 沒超過的就存到這一次的成果，這樣就可以有在固定硬幣數量下所可能拿到的總額是哪些的表，就可以給下一次的操作使用

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        v1, v2, coin = [0], [], 0
        visit = [False] * (amount+1)
        visit[0] = True
        while v1:
            coin += 1
            for v in v1:
                for c in coins:
                    nv = v + c
                    if nv == amount:
                        return coin
                    elif nv > amount:
                        continue
                    elif not visit[nv]:
                        visit[nv] = True
                        v2.append(nv)
            v1, v2 = v2, []
        return -1
