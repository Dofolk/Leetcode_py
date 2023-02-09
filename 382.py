# 這題是設計一個 class 來初始化節點跟隨機取值
# 做法就是先把所有值存起來之後再去隨機從中取值就可以了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.stack = list()
        while head:
            self.stack.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.stack)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
