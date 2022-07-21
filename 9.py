class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        a = []
        while 1:
            a.append(x%10)
            x = x//10;
            if(x == 0):
                break
        for i in range(len(a)//2):
            if(a[i]!=a[len(a)-i-1]):
                return False
        return True
      
# 檢查給定的數值'字串'是不是對稱的
# 所以有付一定都不對稱，先把負數排除
# 注意：0是對稱的，所以條件要寫成<，不能有=
# 然後用一個list紀錄每個十分位的數值
# 最後開始比對頭尾有沒有一樣，所以比對的次數就是總長度//2(不需要小數點)
# 奇數的話中間那一位是對成中心點，所以不用比對
