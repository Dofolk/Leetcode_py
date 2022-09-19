# 這題是要找出字串裡面"最長的回文子字串的長度"是多長
# 做法就是逐一驗證有沒有回文，以目前所在的點為中心，向左右擴張確認是否為奇數或偶數回文
  # 奇數回文就是奇數個數的回文，偶數亦然
  # 這題設定的偶數回文的中心點為長度 L 對半分後左邊的那個位置，也就是 (L-1)/2 的那個位置
# 確認的方法就是用 while 來確認，設定左右邊的邊界，然後確認有沒有超出邊界跟是否一樣
  # 條件滿足後就左右各 +-1 來擴張，重複做到條件不滿足就可以得到中心點拿到的最長回文在哪了

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s)==0: return str()
        def exp(s, L, R):
            while L>=0 and R<len(s) and s[L]==s[R]:
                L -= 1
                R += 1
            
            return R - L - 1
        
        left, right = 0, 0
        for i in range(len(s)):
            l1 = exp(s, i, i)
            l2 = exp(s, i, i + 1)
            M = max(l1,l2)
            if(M > right - left):
                left = i - (M - 1)//2
                right = i + M//2
        
        return s[left:right+1]
