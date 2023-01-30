# 題目會給一個奇偶相交雜的 link list(這很重要，題目一開始有說但我第一次沒注意到掯)，然後把奇數往前放偶數往後放
# 做法就是需要一個 odd 跟 even 下去找出 odd list 跟 even list，然後用一個 even_head 存 even list 的頭，這樣才可以在最後把兩個串起來
# 找的方法就是用 while，odd 就連到 even 後面那個，然後 even 再去聯 odd 後面那個

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        odd = head
        even = head.next
        even_head = even
        while even and odd and even.next and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
