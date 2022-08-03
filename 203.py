# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre = ListNode(-1)
        pre.next = head
        cur = pre
        while cur:
            t = cur.next
            if t is None:
                break
            if t.val == val:
                cur.next = t.next
            else:
                cur = cur.next
        return pre.next
      
# 要移除 link list 裡面特定值的節點
# 做法就是設定一個頭 pre，然後開始往下走看看有沒有一樣的值，有就直接跳過指到再下一個，沒有的話就照路徑往下走
