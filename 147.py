# 這題是給一個 link list，然後要把它做 insertion sort
# 做法就是照著做，先宣告一個變數來儲存整串的頭，然後用一個 cur 下去跑遍整個 list
# 跑一個的時候就做幾件事情，要先來看看 cur 現在指的點要放到哪邊去
  # 如果 cur 的值比 cur.next 的值低的話，那就是代表說原本的list的順序是對的，那我就只要把 cur 往後移去找在下一個東西
  # 如果相比之下大的話，我就先來看一下有沒有比上一次操作的值(p.next.val)還要小，有的話就把 p 移回去 dummy，這樣才能重新找要插入的位置
    # 這邊的 p 就是存上次操作時的點位置
  # 如果比上次操作的值還要大的話就來移動 p 來找要插入的位置
  # 最後就是做 list 的交換，設定一個 new 來存這次交換要插入的點，然後就更新 cur.next, new.next 還有把 new 用 p.next存起來，方便下一次的更新

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head):
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next
