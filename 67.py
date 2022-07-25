class Solution:
    def addBinary(self, a, b) -> str:
        n = max(len(a),len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        c = 0
        ans = []
        for i in range( n - 1, -1, -1):
            if a[i] == '1':
                c += 1
            if b[i] == '1':
                c += 1
            
            if c%2 == 1:
                ans.append('1')
            else:
                ans.append('0')
            c //= 2
        
        if c == 1:
            ans.append('1')
        ans.reverse()
        
        return ''.join(ans)
      
# 做字串的二進位加法
# 先用zfill補一堆0到兩個字串一樣長(也可以用rjust)
# 然後再逐個紀錄相加數值，//2之後有剩就進位保留值
# 最後看有沒有需要多一位出來，再回傳就好了
