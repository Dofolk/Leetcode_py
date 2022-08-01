# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        
        while p1 != p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        
        return p1
      
# 假設兩個串列分別是m+k個及n+k個。WLOG，假設m>n，這樣的話可以把整個串列分成幾個部分：m-n、n、k。
# 第一個指標(p1)跑的過程是 m-n -> n -> k -> n，最後的n是第二串序列的n。
# 第二個指標(p2)跑的過程是 n -> k -> m-n -> n，最後的n是第一串序列的n，除去m前面的m-n個後所留下的n。
# 這樣一來可以看的出來最後都是要跑 n 次的，再加上這裡的 n 都是在兩個序列相交之前，所以只要跑完 n 就一定可以找到相交的序列頭
# 最後要注意的事情是判斷是裡面判斷的是當下的 None 與否，不能寫成判斷 next 是不是 None ，不然的話等跑最後一次n的時候 p1 p2 會又變換到另一個序列去，永遠不停地變換跟跑
