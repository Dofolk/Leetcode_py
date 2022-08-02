class Solution:
    def reverseBits(self, n: int) -> int:
        s = format(n,'b').zfill(32)
        s = s[::-1]
        return int(s,2)
      
# 這題要做 bit reverse
# 這裡使用 format + zfill，確保轉換之後的二進制字串會有足夠32的位元
# 然後再用原始的sting reverse [::-1]取得reverse的字串
# 最後輸出數字就完成了
