# 這題是給兩個 Link list 代表一個數字，(1->2->3 = 123)，然後把兩個數字相加後回傳 Link list
# 做法就是直接把數字拿到，然後重新建立一個 link list 回傳就好了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1, v2 = 0, 0
        
        while l1:
            v1 = v1 * 10 + l1.val
            l1 = l1.next
        while l2:
            v2 = v2 * 10 + l2.val
            l2 = l2.next
        
        dummyList = dummy = ListNode(0)
        for val in str(v1+v2):
            dummy.next = ListNode(val)
            dummy = dummy.next
        
        return dummyList.next
