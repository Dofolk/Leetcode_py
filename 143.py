# 這題是給一個 link list，然後把整串對折，形成 1->n->2->n-1->3->n-2->... 的順序
# 做法就是用 fast slow two pointer 先找中間點，然後從中間點開始做 list 的反轉
# 反轉完之後就按照順序逐個連接好就可以了！

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
