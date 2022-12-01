# 這題是給兩個陣列，一個是 gas，一個是 cost
# 選擇一個 index 後依照序號開始往下走，先加 gas 後再扣掉所需的 cost，看看從哪個點開始走可以走完(中途沒油就裂開)
# 做法就是從頭開始，先看看第一步有沒有辦法走出去(也就是第一次加油要比扣油還多，不然沒油可以動)
# 可以走的話就開始望下確認，用一個 res 來存說目前走法的話油香會有多少油，一直到油箱沒油的時候做更新，把 res 歸零，把 start 改成第 i+1 個
  # 因為你這樣走的話都可以在正數起頭走到變成負的，代表這一區裡面的起點一定都會走出負數，所以直接跳到 i+1個去
# 如果沒得走就往下更新下一個起點繼續算
# 最後還要多確認一下，全部的油夠不夠走

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = start = overall = 0

        for i in range(len(gas)):
            s = gas[i] - cost[i]
            res += s
            overall += s
            if res < 0:
                res, start = 0, i + 1
        
        return start if overall>=0 else -1
