# 這題是去設計一個有兩種操作的 class，一個操作是去存數字，另一個操作就是給一個數字 k ，然後回傳前 k 步添加的所有數字的相乘結果
# 想法就是用 prefix 來記錄前面遇到的所有直乘積的結果，然後遇到 0 就清空，所以在 add() 就是做這些事情
# 等需要找數字的時候就先做確認，看看要找的長度 k 有沒有超過目前 prefix 的長度，有的話就代表說有吃到 0，直接歸0就好
# 沒有的話就依據長度看是要給最後的乘積結果還是要去做相除拿結果

# ===== Question =====
# 設計一個 ProductOfNumbers 類別，初始時數列為空，add(num) 會把 num 加到數列尾端。
# getProduct(k) 要回傳數列中最後 k 個數字的乘積，題目保證查詢時至少已有 k 個數字。

# ===== Thoughts =====
# 這題就是乘法版本的 prefix，然後再遇到 0 的時候就更新一輪 prefix 的陣列
# 這邊還有一個是因為遇到 0 的時候就會更新 prefix 的陣列，所以每次要 getProduct的時候
# 如果有遇到要 get 的時候就檢查 get 的長度到哪邊，如果超出紀錄長度的話就直接回傳 0
# 沒有超過就直接做 prefix 的乘法相除就好

class ProductOfNumbers:

    def __init__(self):
        self.prefix_prod = []
        self.prod = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.prod *= num
            self.prefix_prod.append(self.prod)
        else:
            self.prefix_prod = []
            self.prod = 1

    def getProduct(self, k: int) -> int:
        if k > len(self.prefix_prod):
            return 0
        elif k == len(self.prefix_prod):
            return self.prefix_prod[-1]
        else:
            return self.prefix_prod[-1] // self.prefix_prod[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
