# 這題是要去找給的IP是不是合法的
# 做法就是直接去作條件篩選
  # 第一篩一定都是篩長度，IPv4有4個, IPv6有8個
  # IPv4的條件就是要處理掉: 空值, '01'的狀況, 不是常數以及太大的數字
  # IPv6的條件就是要處理掉: 空值, 給的子位址太長(12345)以及不是16進位的字

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            ipv4 = queryIP.split('.')
            if not len(ipv4) == 4:
                return 'Neither'
            for s in ipv4:
                if s == '' or (s[0] == '0' and len(s) != 1) or not s.isdigit() or int(s) > 255:
                    return 'Neither'
            return 'IPv4'
        elif ':' in queryIP:
            ipv6 = queryIP.split(':')
            if not len(ipv6) == 8:
                return 'Neither'
            for s in ipv6:
                if s == '' or len(s) > 4 or not all(c in hexdigits for c in s):
                    return 'Neither'
            return 'IPv6'
        return 'Neither'
