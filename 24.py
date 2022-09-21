# 這題是要把 link list 的兩兩節點做調換
# 作法有兩個，一個是遞迴，另一個是迴圈
# 遞迴就是把 head head.next 先拿好，然後給 first.next 的值是再call一次函數(自己函數代second.next進去)的結果(也就是下一個pair的頭)
  # 最後再回傳second跟調整各自next的點就可以了
# 魂圈的話就是先宣告一個空頭，指向前一個pair的尾巴，然後用 while迴圈來操作，先把前一個pair的尾巴接上second
  # 然後再調整prevnode為first、second.next變成first，最後再更新下一個迴圈要用的head就可以了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second

# 2
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        prev_node = ListNode(0)
        prev_node = dummy
        
        while head and head.next:
            first = head
            second = head.next
            
            prev_node.next = second
            first.next = second.next
            second.next = first
            
            prev_node = first
            head = first.next
            
        return dummy.next
            
        return dummy.next
