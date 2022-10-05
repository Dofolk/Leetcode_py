# 這題是要把給定的字串變成 IP 位址之後輸出出來
# 做法就是用 backtrack 來做，IPv4 有四個地方可以放數字，所以就是一格一格填好之後回傳就可以了
# 所以就會需要幾個變數，一個是目前剩下的數字有哪些(string)，一個是目前是要填哪一個(block)，以及現在組好的位址長怎樣(ip)
# 然後就開始做判斷，像是到第三格的時候剩下超過4個數字或沒半個數字，或者是剩下的數字開頭是0，這一類的有誤IP
# 接著就看看有沒有到第四格，有的話就判斷一下能不能當成 IP，可以就收工，不能就掰掰
# 如果沒有到第四個的話就用 for 開始放1,2,3個數字在格子裡面，判斷合不合法後就可以再呼叫一次來處理後面剩下的字串了

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n<4 or n>12: return str()

        res = []
        def ips(string, block, ip):
            if len(string) == 0 or ( len(string) > 3 and block == 3 ):
                return
            if block < 3:
                for i in range(3):
                    doing_now = string[:i+1]
                    rest_of_string = string[i+1:]
                    if 0 <= int(doing_now) <= 255:
                        if doing_now[0] == '0' and len(doing_now) > 1:
                            break
                        ips(string[i+1:], block + 1, ip + doing_now + ".")
            else:
                if 0 <= int(string) <= 255 :
                    if not( string[0] == '0' and len(string) > 1):
                        res.append(ip + string)
            return
        
        
        ips(s, 0, "")
        return res
