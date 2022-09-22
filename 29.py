# 這題是要在不使用乘除及mod的情況下找商數
# 做法就是用加法跟while迴圈來做，在做迴圈的時候可以多一層while，目的是要增加除數，變成二倍除數、三倍除數或更高的，比較快可以找到商數
# 另外，這邊也先把所有數字變成正數，這樣比較好操作

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg1, neg2 = 0, 0
        if dividend < 0:
            neg1 = 1
            dividend = -dividend
        if divisor < 0:
            neg2 = 1
            divisor = -divisor
        if (neg1+neg2 == 1):
            neg_sign = True
        else:
            neg_sign = False
            
        if divisor == 1:
            if neg_sign: dividend = -dividend
            if dividend > pow(2,31) - 1: return pow(2,31) - 1
            if dividend < -pow(2,31) : return -pow(2,31)
            return dividend
        n = 0
        while divisor <= dividend:
            N = 1
            dvr = divisor
            while dividend>=dvr:
                n += N
                dividend -= dvr
                dvr += dvr
                N += N
        
        return -n if neg_sign else n
