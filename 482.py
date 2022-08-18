# 這題是要把字串變成大寫，然後按照給定的長度做區分
# 長度k的字串放在最後面，餘下的字串數量就放在最前面

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace('-','')
        if len(s) <= k: return s
        r = len(s)%k
        if not r:
            return '-'.join( s[i:i+k] for i in range(0,len(s),k))
        else:
            return ''.join(s[:r]) + '-' + '-'.join( s[i:i+k] for i in range(r,len(s),k))
