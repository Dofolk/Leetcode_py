# 這題是給一個 link list，然後把它變成遞增的
# 想法就跟 merge sort 很像，先用 fast slow two pointer 來找出中間的位置，然後把一個 link list 切成兩分(尾端加 None )，然後再往下去找下兩段的結果，最後回傳 merge 的成果
  # 所以簡單來說就是，找中點，分成兩段做好，回傳 merge 的結果
# 在 merge 的部分就比較簡單，兩個 link list 先看看有沒有存在，不存在就直接回傳其中一邊就好了，存在話就可以開始做左右比較後串再一起，最後回傳 dummy.next 就可以了
  # 這邊在做 dummy 的時候要另外宣告一個遍書來跑，不然頭會不見

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        slow.next = None
        L, R = self.sortList(head), self.sortList(start)
        return self.merge(L,R)
    
    def merge(self, L, R):
        if not L or not R: return L or R
        dummy = p = ListNode(0)
        while L and R:
            if L.val < R.val:
                p.next = L
                L = L.next
            else:
                p.next = R
                R = R.next
            p = p.next
        p.next = L or R
        return dummy.next
