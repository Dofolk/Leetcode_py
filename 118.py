class Solution:

# Solution 1
    def generate(self, numRows: int) -> List[List[int]]:
        factorial = [1]
        s = 1
        for i in range(numRows):
            s = s*(i+1)
            factorial.append(s)
        
        ls = []
        for m in range(numRows):
            ls_tmp = []
            for n in range(m+1):
                v = int(factorial[m]/(factorial[n]*factorial[m-n]))
                ls_tmp.append(v)
            ls.append(ls_tmp)
        
        return ls
      
# 做帕斯卡三角出來
# 這邊用排列組合 C算法做出來的
# 先做出C table(factorial)出來再一條一條做乘除計算就好了
# 另一種做法就是位移做加減，如下

# Solution 2
def generate(self, numRows: int) -> List[List[int]]:
        ls = [[1]]
        pre = [1]
        
        for m in range(numRows-1):
            ls_tmp = pre[:]
            ls_tmp.append(0)
            for i in range(m+1):
                ls_tmp[i+1] += pre[i]
            ls.append(ls_tmp)
            pre = ls_tmp
        return ls
