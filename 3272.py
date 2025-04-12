# === Description ===
# 題目說有個整數性質叫 k-回文，指該整數是回文也是 k 的倍數，然後說一個數是好的數字代表說可以透過調整順序以達成 k-回文
# 接著給定數字 n 及指定 k，問 n 位數的數字中，總共有幾個 "好的 k-回文數字"
#
# === Thought ===
# 這邊可以從回文的性質下手，回文的話會有左右各一半的數字做序列對應，所以這邊可以把 n 對半分去找出這個一半長度的數字
# 所以先找基礎長度的數字會是從 base_num 開始，n-1 是確保奇數長度也可以找，然後把找到的基礎數字做對應就可以用 record 來記錄這個數字
# 這邊可以用一個 skip 來記錄目前處理的長度 n 是不是奇數，來看看組合出數字的時候要不要替除掉第一個數字 ex:123 -> 32123, 踢掉1
# 還有，record 要存起來的數字記得先做排序，以方便說 rearrange 之後的結果是同一個，避免重複計算
# 等找到所有數字之後，就可以用排列組合的想法來操作，對於每個記錄下來的數字先統計 0~9 個出現幾次
# 然後可以透過 (n-0出現次數)! / 重複項! ，全部加起來就可以了！
# === Code ===
#
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        record = set()
        base_num = 10 ** ((n - 1) // 2)
        skip = n & 1

        for idx in range(base_num, base_num * 10):
            s = str(idx)
            s += s[::-1][skip:]
            if int(s) % k == 0:
                record.add("".join(sorted(s)))
        
        count = 0
        factorials = [math.factorial(num) for num in range(n + 1)]

        for s in record:
            digit_count = [0] * 10
            for char in s:
                digit_count[int(char)] += 1
            total_choices = (n - digit_count[0]) * factorials[n - 1]
            for val in digit_count:
                total_choices //= factorials[val]
            count += total_choices
        return count
