# === Description ===
# 這題是給一個數字序列 nums，代表每個編號點的數值，以及一個數字 k，還有 edges 表示兩點有相連
# 然後題目有說邊的數量會是 lenght(nums) - 1，並且可以組成一個合法的 tree
# 每次都可以選擇一個邊對兩個點做 point = point XOR k，然後可以做任意次，問最大能讓所有點總和變得多大
# 
# === Thought ===
# 因為是合法的 tree 以及邊數量比點數量少 1，所以不會有迴圈的出現，以及每一對點都可以找到一條路徑相連彼此
# 然後因為可以做任意次，所以其實只要考慮每個點在 xor 之後執會不會變大就好
# 因為每一對點都有路徑相連+可以做無限次數 => 一定會有套或不套用的組合讓兩個點都可以拿到最大效益
# 所以就可以先把數字總和加起來，然後去算 xor 之後跟原始數值的差異，把正數兩兩分組起來加就好了
# 如果遇到正數數量不是2的倍數時，就去考慮加最大的負數跟減最小正數哪個比較划算，選擇讓數值損失最小的就對了
#
# === Code ===

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        diffs = [(num^k) - num for num in nums]
        positive = [val for val in diffs if val >= 0]
        res = sum(nums) + sum(positive)
        if len(positive) % 2 == 0:
            return res
        
        maxNeg = max((val for val in diffs if val < 0), default = float("-inf"))
        minPos = min(positive)
        return res + max(maxNeg, -minPos)
