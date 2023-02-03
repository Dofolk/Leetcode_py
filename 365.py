# 這題就是4公升水桶問題 ( 貝祖定理 )
# 如果兩個水桶相加都小於了就不用講一定是Fail(這個要先做一次判斷，不然像是1 2 4就會裂開)
# 然後根據貝祖定理，目標值一定要是最大公因數的倍數，所以就用 % 來看看有沒有符合

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # x = jug1Capacity, y = jug2Capacity, z = targetCapacity
        return False if x + y < z else not z % math.gcd(x,y)
