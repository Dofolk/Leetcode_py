# 這題就是看給的字串有有沒有出現過兩個A或是連續三個L
# 作法1是比較暴力解法，直接 for loop 跑遍一次，同時確認有沒有累計2A跟連續LLL
# 做法2就用 python 內建的 count() 跟 in 來確認有沒有出現目標字串或字元

class Solution:
  
# Solution 1
    def checkRecord(self, s: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count += 1
                if count >= 2: return False
            if s[i] == 'L' and i+2<len(s):
                if s[i:i+3] == 'LLL':
                    return False
        return True

# Solution 2
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s
