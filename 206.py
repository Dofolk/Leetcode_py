# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            
        return pre
      
# 這題是要做 link list reverse，一個 while 做完，想法就跟 C 的交換類似，用 temp 來做個暫存紀錄在做個 next 指標交換就可以了
