# 這題是給兩個數字 num1 跟 num2，再給一個數字 x，x 的二進位表示 1 的數量跟 num2 一樣，問 x 的數值是多少時，x XOR num1 會有最小值
# 這題的想法就是，要 XOR 最小的話就是把有 1 存在的地方一樣也放 1，然後二進位以最後面的 0 開始替換，這樣做出來的話就會是最小的
# 所以就先看一下 1 的數量，如果一樣就直接回傳 num1，這樣 XOR 會 = 0
# 接著就是看 x 跟 num1 的 1 數量差多少，根據差距由後往前 0 換 1 或是 1 換 0

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        binary1 = format(num1, 'b')
        bits1 = binary1.count('1')
        bits2 = format(num2, 'b').count('1')
        if bits1 == bits2:
            return num1
        if bits2 >= len(binary1):
            return int('1' * bits2, 2)
        ans = list(binary1)
        diff = bits2 - bits1
        point = -1
        if diff > 0:
            while diff:
                if ans[point] == '0':
                    ans[point] = '1'
                    diff -= 1
                point -= 1
        elif diff < 0:
            diff = -diff
            while diff:
                if ans[point] == '1':
                    ans[point] = '0'
                    diff -= 1
                point -= 1
        return int(''.join(ans),2)
