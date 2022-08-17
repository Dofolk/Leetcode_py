# 這題就是說有個手錶只有二進位表示法，現在給定亮燈的數量(不含pm燈)，問可以表示那些時間點
# 做法就是把0~59的所有二進制為1的數目算出來，然後就開始一個一個找，從0時開始到11時

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        num2 = [bin(i).count("1") for i in range(60)]
        for i in range(12):
            hr = num2[i]
            for n in range(60):
                m = num2[n]
                if hr+m == turnedOn:
                    ans.append(f"{i}:{n:02d}")
                    
        return ans
