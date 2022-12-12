# 這題是給兩個數字，然後把除法結果輸出成字串出來
# 做法就是用 divmod 做除法解果存起來，然後確認有沒有重複，用 *10再除來做運算跟確認重複
# 最後就找依下重複的位置後插括號進去，以及最後用 rstrip() 來移除 '.'，遇到整除的狀況就會需要，因為最一開始的時候給他加了小數點，而後面還把 (0) 給替換不見

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        seen = []
        result = [sign+str(n),'.']
        while remainder not in seen:
            seen.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))
        idx = seen.index(remainder)
        result.insert(idx+2,'(')
        result.append(')')
        return ''.join(result).replace('(0)','').rstrip('.')
