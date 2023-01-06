# 這題是給一串數字串，然後看看把數字拆解之後能不能寫出個計算式 A+B+...+N=M
# 做法就是直接算，分成幾個部份來做相加，給三個位置標點找出兩個數字，然後去相加看能不能拿到最後的成果
# 在做每一步的時候都要確認不會出現 '02' '03' 等等的非正常數字


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        L = len(num)
        if not num or L < 3:
            return False
        
        for i in range(1, L):
            if i > 1 and num[0] == '0':
                break
            for j in range(i+1, L):
                st, nd, rd = 0, i, j
                if num[nd] == '0' and rd > nd + 1:
                    break
                while rd < L:
                    res = str(int(num[st:nd])+int(num[nd:rd]))
                    if num[rd:].startswith(res):
                        st, nd, rd = nd, rd, rd+len(res)
                    else:
                        break
                if rd == L:
                    return True
        return False
