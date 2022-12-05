# 這題是給一個有 cycle 的 link list，然後把 cycle 的頭找出來回傳，沒有 cycle 就回傳None
# 這題來用 fast and slow two pointer來做，假設頭到 cycle 頭是距離 A，兩個指標在迴圈的 B 遇到，快的指標走了2A+2B步了，慢的走了A+B，所以 A+B+N=2A+2B，N就是cycle一圈的距離
# 所以這算起來全部有2A+B，扣掉前面走的A+B，剩下A補完就可以找到頭了
# 所以先兩個指標去跑，跑完之後再從頭找個指標再跑個A步就找到點了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow
        return None
