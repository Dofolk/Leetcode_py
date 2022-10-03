# 這題是要把 link list 裡面有重複的點全部移除
# 做法就是跑一遍，然後前後兩點如果一樣的話就用一個回圈跑到重複的底，然後再把前面的節點連線過來就可以了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head

        dummy = pre = ListNode(next = head)
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        
        return dummy.next
