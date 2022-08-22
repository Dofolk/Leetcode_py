# 這題是在算中毒時間，重複被攻擊的時候中毒時間會刷新，給一個 timeSeries 說攻擊時間點以及中毒多久(duration)
# 第一個做法是減法，攻擊次數*中毒時間就是最大的時間，看那些時間點有重疊到就扣除掉
# 第二個加法是加法，看攻擊間距有沒有大於 duration，沒有的話就加攻擊間距時間上去，有的話就加 duration 上去，最後再補一個最後一次攻擊的一個 duration

class Solution:
  
# Solution 1
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0
        v = len(timeSeries)*duration
        for i in range(len(timeSeries)-1):
            vt = timeSeries[i+1]-timeSeries[i]
            if vt < duration:
                v -= duration - vt
        
        return v
      
# Solution 2
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0
        L = len(timeSeries)
        v = 0
        for i in range(L-1):
            v += min(timeSeries[i+1]-timeSeries[i], duration)
        return v+duration
