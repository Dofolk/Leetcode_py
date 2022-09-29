# 這題是要做 link list 的旋轉，轉一次就是把尾端拉到最前面一次，最後看看整個 list 變成怎樣
# 作法就是先找一下有多長，順便把 link list 做成 circle (如果長度>1的話)，然後就開始找到數第 k 個點來把 circle 解開
# 這邊 k 要先做一次同餘，以節省後面在找節點的時候要跑的 for 次數，最後在找好的點做斷點回傳就可以了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0: return head
        count = 0
        cur = head
        while cur:
            count += 1
            if cur.next is None and count>1:
                cur.next = head
                break
            cur = cur.next
        if count <= 1: return head
        cur = head
        k %= count
        for _ in range(abs(count-k-1)):
            cur = cur.next
        pre = ListNode(0)
        pre.next = cur.next
        cur.next = None
        
        return pre.next
