# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        cur = head
        while cur:
            ls.append(cur.val)
            cur = cur.next
        l = len(ls)
        if l==1:
            return True
        for i in range(l//2):
            if ls[i]!=ls[l-i-1]:
                return False
        return True
      
# 這題是看 link list 有沒有對稱回文
# 做法就是直接走一遍拿到所有值
# 再跟之前一樣對半比對
# 算是暴力解法
