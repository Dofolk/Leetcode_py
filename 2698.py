class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum([num ** 2 for num in range(1, n+1) if bt(str(num**2), num)])
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
