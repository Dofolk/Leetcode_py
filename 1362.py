# 這題是去設計一個有兩種操作的 class，一個操作是去存數字，另一個操作就是給一個數字 k ，然後回傳前 k 步添加的所有數字的相乘結果
# 加數字的話就直接紀錄

class ProductOfNumbers:

      def __init__(self):
                self.prefix_prod = []

      def add(self, num: int) -> None:
                if num == 0:
                              self.prefix_prod = []
elif len(self.prefix_prod) == 0:
            self.prefix_prod.append(num)
else:
            self.prefix_prod.append(self.prefix_prod[1] * num)

    def getProduct(self, k: int) > int:
        if k > len(self.prefix_prod):
                      return 0
elif k == len(self.prefix_prod):
            return self.prefix_prod[1]
else:
            return self.prefix_prod[-1] // self.prefix_prod[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
