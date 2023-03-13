# 這題是給一個 link list，每個節點有 "值、前、後、子" 四個參數，然後要把這樣的 list 攤平
# 攤平的方式就是遇到有"子"的就給他當成塞進那個節點並拉長開來，拉好之後再把原本該節點的後一個接到子序列的尾巴
# 做法就是用 DFS 來找有沒有次一個節點以及子序列的尾巴在哪裡，找到之後開始對其參數做調整就可以了

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        def dfs(node):
            while node:
                Next = node.next
                if not Next and not node.child:
                    return node
                elif node.child:
                    node.next = node.child
                    node.child.prev = node

                    child_tail = dfs(node.child)
                    node.child = None

                    if Next:
                        Next.prev = child_tail
                        child_tail.next = Next
                    else:
                        return child_tail
                    
                node = Next
        
        dfs(head)
        return head
