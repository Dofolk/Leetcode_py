# 這題是要把一個 link list 依照數字做重新排列且順序不能改變，所以就是比木小的就依序放在前面，後面補上比目標值大的數字
# 做法就是宣告兩個 link list 的頭，然後一個紀錄前半段(比目標小的)，另一個紀錄後半段，然後再逐個點跑一遍分別記錄好之後就可以做整理跟輸出了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        front, back = ListNode(0), ListNode(0)
        front_prev, back_prev = front, back
        
        while head:
            if head.val < x:
                front_prev.next = head
                front_prev = front_prev.next
            elif head.val >= x:
                back_prev.next = head
                back_prev = back_prev.next
            head = head.next
        front_prev.next = back.next
        back_prev.next = None
        return front.next
