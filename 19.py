# 這題是要移除 link list 倒數第 n 個節點
# 作法有兩個
# 一個是先走過一遍看有多長再走長度減 n 的點之後移除節點
# 另一個是類似 two pointer，讓其中一個先走 n 步，之後兩個 pointer 都一起走，直到第一個到底之後就可以找到要移除的節點在哪了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = ListNode(0)
        cur.next = head 
        length = 0
        first = head
        while first:
            first = first.next
            length += 1
        length -= n
        first = cur
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return cur.next
        
# 2
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = ListNode(0)
        cur.next = head
        p1 = cur
        p2 = cur
        
        for i in range(n+1):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next
        
        return cur.next
