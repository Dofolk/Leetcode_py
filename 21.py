# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        
        prev.next = l1 if l1 is not None else l2

        return prehead.next
      
# 給定兩個list, L1,L2
# 每個list裡面都有一堆定義好的ListNode(每個list的點都是ListNode)
# 這題就是要把L1,L2的next連結做好，最後回傳連結的線頭
