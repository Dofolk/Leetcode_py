# 這題是給定一個數字 n 代表數字喂元移動的數量，然後便往前確認喂元不同的位置並轉變成數字
# 做法就是照著做，可以用 python 的位元運算符號來操作，操作過會可以直接輸出成 int 

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if not n: return [0]
        res = [0,1]
        for i in range(2,n+1):
            for j in range(len(res)-1, -1, -1):
                res.append( res[j]| 1<<i-1)
        return res
