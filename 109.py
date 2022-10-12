# 這題是要把一個直線的 link list 改成 BST
# 做法就是先判斷目前的節點存不存在以及後一個節點存不存在，存在的話再開始做，不存在就回傳
# 然後就開始找中間節點，用 while 以及二倍跳來找，找到中間點之後就可以建立點跟回傳

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head: return
        if not head.next: return TreeNode(head.val)
        
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None

        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        
        return node
