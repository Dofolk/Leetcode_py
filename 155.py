# 這題是要宣告一個叫 MinStack 的東西，他的函數如下所示
# 這邊會宣告一個 minStack 來存每次操作的時候最小的值是多少，所以長度會跟 stack 一樣，然後最小的值也會跟著被 pop 掉，這樣才能做到 minStack 最後一個值永遠是目前 stack 的最小值

class MinStack:

    def __init__(self): # 宣告 stack 的樣子
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None: # 就是把值放進stack裡面
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None: # 移除最後一項
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int: # 回傳stack最上面的值是多少
        return self.stack[-1]

    def getMin(self) -> int: # 回傳目前 stack 裡面最小的值是多少
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
