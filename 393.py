# 這題是要看看給定的 list 有沒有合 UTF-8 的標準規定
# UTF-8 可以看 wiki
# 稍微講一下就是，遇到的第一個數字的二進位表示法中，最前面的連續出現的 1 的數量 (n) 代表說在第二個數字開始的二進位表示連續 n-1 個是以10為開頭的數字
  # 也就是說現在第一個遇到的是 1110XXXX的話，就代表後面有兩個 10xx，再後面的數字就不能有10開頭的
  # 而最前面1的數量最多4，所以超過4也不可以
  
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        
        for byte in data:
            if byte >= 128 and byte <= 191:
                if not count:
                    return False
                count -= 1
            else:
                if count:
                    return False
                if byte < 128:
                    continue
                elif byte < 224:
                    count = 1
                elif byte < 240:
                    count = 2
                elif byte < 248:
                    count = 3
                else:
                    return False
                    
        return count == 0
      
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cur = 0
        for val in data:
            if cur == 0:
                if val >> 5 == 0b110:
                    cur = 1
                elif val >> 4 == 0b1110:
                    cur = 2
                elif val >> 3 == 0b11110:
                    cur = 3
                elif val >> 7:
                    return False
            else:
                if val >> 6 == 0b10:
                    cur -= 1
                else:
                    return False
        return cur == 0
