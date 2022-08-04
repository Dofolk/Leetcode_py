# 這題是要用 stack 來模擬 queue 的操作
# 一樣用上基本的 python 內建函數就可以完成了

class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        return None

    def pop(self) -> int:
        return self.queue.pop(0)
        ''' 這邊也可以用 del
        v = self.queue[0]
        del self.queue[0]
        return v
        '''

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if self.queue:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
