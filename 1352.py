# 這題是去設計一個有兩種操作的 class，一個操作是去存數字，另一個操作就是給一個數字 k ，然後回傳前 k 步添加的所有數字的相乘結果
# 想法就是用 prefix 來記錄前面遇到的所有直乘積的結果，然後遇到 0 就清空，所以在 add() 就是做這些事情
# 等需要找數字的時候就先做確認，看看要找的長度 k 有沒有超過目前 prefix 的長度，有的話就代表說有吃到 0，直接歸0就好
# 沒有的話就依據長度看是要給最後的乘積結果還是要去做相除拿結果

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
