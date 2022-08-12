# 這題是要把 n 前面的所有數字，看看其二進位的 1 總和
# 第一種方法暴力解法，就一個一個做計算
# 第二種做法就是除以二看有沒有餘數，有的話就加一，沒有的話就直接找 list 裡面 i//2 的值就可以了
# 第三種方法就是用 string.count() 來算有幾個 1 

class Solution:
  
# Solution 1
    def countBits(self, n: int) -> List[int]:
        l = [0]
        for i in range(1,n+1,1):
            v = 0
            s = format(i,'b')
            for i in s:
                if i == '1':
                    v += 1
            l.append(v)
            
        return l
      
# Solution 2
    def countBits(self, n: int) -> List[int]:
        l = [0]
        for i in range(1,n+1,1):
            if i%2 != 0:
                l.append(l[i//2]+1)
            else:
                l.append(l[i//2])
        return l

# Solution 3
    def countBits(self, n: int) -> List[int]:
        l = [0]
        for i in range(1,n+1,1):
            s = format(i,'b')
            l.append(s.count('1'))
        return l
