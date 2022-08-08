# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node.next
        node.val = cur.val
        node.next = cur.next

        
# 這題要把一個 link list 其中一個點移除掉
# 題目的部分只給要移除的點，所以就是把下一個的點內容往前拉到當下的點， next 再往後一個就可以了
