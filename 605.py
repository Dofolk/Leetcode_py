# 這題是要種樹，相鄰不種樹，所以給了一個 list 來表示哪邊有種樹，最後給個預計要種樹的量能不能種下去
# 做法就是做最大能種樹的量，左右判斷一下能不能種，可以就種，不能就跳過下一個

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                L_scan = (i==0) or (flowerbed[i-1]==0)
                R_scan = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                if L_scan and R_scan:
                    flowerbed[i] = 1
                    count += 1
                    if count>=n:
                        return True
        return count>=n
