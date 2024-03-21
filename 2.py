# 這題是要做把兩個 link list 做相加，而 link list 為個位數、十位數、百位數...等依序連結下去
# 所以就是需要一個 carry 來記錄看看有沒有進位，然後再往下操作
# 這邊有使用到說，當 list1 跟 list2 沒東西的時候就是直接給值為0，可以不用去考慮長度問題
# 然後需要額外宣告一個 list 來記錄結果，因為題目要求要回傳ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        carry = 0
        while l1 or l2 or carry :
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            S = v1 + v2 + carry
            carry = S//10
            cur.next = ListNode(S%10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
