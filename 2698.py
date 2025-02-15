# 這題是說有個數字叫 punishment number，就是 num^2 的數字做連續組合相加之後等於 num
# 舉例來說，36 * 36 = 1296，1+29+6=36
# 這題的想法就是取找出所有可能性來相加看看有沒有機會做出來，找所有可能性的法就是用 backtrack
# 按照數字逐個從左到後去找，第一步就是先抓一個數字起來，然後去做 backtrack(DFS) 找右邊剩下的數字，能有多少組合以及能不能達到目標數字
# 當第一步找完之後就去找，當左邊是兩個數字時，右邊剩下的數字能不能達到，以此類推到全部走完一輪
# 右邊數字的找法就是，先確認有沒有數字能操作，以及當前數字有沒有跟目標一樣
# 確認完基本條件之後，就開始對這串數字做一樣的操作，抓著左邊的數字往下去找右邊的

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum([num ** 2 for num in range(1, n + 1) if bt(str(num ** 2), num)])
@lru_cache(None) 
def bt(s, target):
    if len(s) == 0:
        return target == 0
    if int(s) == target:
        return True
    for idx in range(len(s)):
        if bt(s[idx + 1:], target  int(s[:idx + 1])):
            return True
    return False
