# 這題是要把 link list 中間的一段給反轉
# 法做法就是先定位出中間段的前一個，然後進入中間段之後就開始做反轉，最後的時候把頭尾給接好就可以了
# 沒有很困難，用 for 就可以了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        
        dummy = ListNode(0,next=head)
        prev = dummy
        for i in range(left-1):
            prev = prev.next
        
        reverse = None
        cur = prev.next
        for i in range(right-left+1):
            N = cur.next
            cur.next = reverse
            reverse = cur
            cur = N
        
        prev.next.next = cur
        prev.next = reverse
        return dummy.next
        
