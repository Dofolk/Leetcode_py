# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 第一個方法就是用一個list來存走過的路有哪些，然後再看看有沒有走過
# 第二個方法就是把每個走過的點都變成最大的val(float inf)，到時候就知道這個點有沒有走過了

class Solution:

# Solution 1
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ls = []
        
        while head:
            if head.next in ls:
                return True
            ls.append(head.next)
            head = head.next
        return False

# Solution 2
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        M = float('inf')
        temp = head
        
        while temp:
            if temp.val == M:
                return True
            temp.val = M
            temp = temp.next
        
        return False      
