# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev = head
        n = head.next

        while n:
            if prev.val == n.val:
                prev.next = n.next
                n = n.next
            elif prev.val != n.val:
                n = n.next
                prev = prev.next

        return head
      
# 做 link list，然後要把原list的重複值的部分移除掉
# 要注意第一個if來判斷input為空列的時候
# 這個就一個一個往下做.next的更新就好了
# 要注意做更新的時候要拿到對的next
