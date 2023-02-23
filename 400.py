# 這題是給一個目標位置，然後去找看看該位置上的數字是多少，搜尋的目標是 1234567891011....，把數字全部串在一起的字串
# 做法就是去看看大小，是會落在個位數、十位數還是百位數等等的(size*step)，然後再去做每個參數的更新調整，隨著位數增加而遞增
# 最後就可以把目標位置 -1 (數量計算的偏差) 除上 size 就可以知道是落在多少位數的第幾面，再用 mod 來找出是該數字的第幾個位數

class Solution:
    def findNthDigit(self, n: int) -> int:
        start, size, step = 1, 1, 9
        while n > size * step:
            n, start, size, step = n - size * step, start * 10, size + 1, step * 10
        return int(str(start + (n-1)//size )[(n - 1) % size])
