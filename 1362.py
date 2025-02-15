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
