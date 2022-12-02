# 這題是給一串點，然後複製出來
# 做法就是先做一遍，把一直線的點先做好連好(.next)
# 然後有一串之後，就可以把原本的 random 點做好連結就可以了(因為已經有所有的點了，只要把點連好就可以了)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs1(head,D):
            if not head: return None
            root = Node(head.val)
            D[head] = root
            root.next = dfs1(head.next, D)
            return root
        def dfs2(head, root, D):
            if not head or not root: return
            root.random = None if not head.random else D[head.random]
            dfs2(head.next, root.next, D)
        
        D = dict()
        root = dfs1(head, D)
        dfs2(head, root, D)
        return root
