# 這題是要算兩個字串的 ?A?B，就是對數字有沒有一樣跟位置
# 作法有兩個，第一個是先找 A 有多少之後再去找 B，用 Counter 來記錄目前還有多少數字可以用
# 第二個是用 map()，引入 operator package，然後用 eq 來找出 A，然後再用 Counter 去找所有的數字，最後回傳的時候再扣掉 A 就可以ㄌ

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        L = len(guess)
        C = collections.Counter(secret)
        A, B = 0, 0
        for i in range(L):
            if guess[i] == secret[i]:
                A += 1
                C[guess[i]] -= 1
        
        for i in range(L):
            if guess[i] == secret[i]: continue
            if guess[i] in secret and C[guess[i]] > 0:
                B += 1
                C[guess[i]] -= 1
        
        return str(A)+'A'+str(B)+'B'
      
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = sum(map(operator.eq, secret, guess))
        
        c1 = collections.Counter(secret)
        c2 = collections.Counter(guess)
        
        b = 0
        for key in c1.keys():
            b += min(c1.get(key,0), c2.get(key,0))
        
        return str(a) + 'A' + str(b-a) + 'B'
