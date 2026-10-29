# ===== Question =====
# 題目給一棵無向樹，每個節點上都有一個小寫英文字母。
# 你會收到兩種操作指令：修改某個節點的字母，或查詢兩個節點之間的唯一路徑。
# 每次查詢要判斷：這條路徑上所有節點的字母，重新排列後能不能組成回文，並回傳 True 或 False。

# ===== Thoughts =====
# 這題直接左轉靈神，宣告陣亡

# Methos - Fenwick + LCA + DFS
# From 灵茶山艾府
class FenwickTree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)  # 使用下标 1 到 n

    # a[i] ^= val
    # 1 <= i <= n
    # 时间复杂度 O(log n)
    def update(self, i: int, val: int) -> None:
        t = self.tree
        while i < len(t):
            t[i] ^= val
            i += i & -i

    # 计算前缀异或和 a[1] ^ ... ^ a[i]
    # 1 <= i <= n
    # 时间复杂度 O(log n)
    def pre(self, i: int) -> int:
        t = self.tree
        res = 0
        while i > 0:
            res ^= t[i]
            i &= i - 1
        return res

class LcaBinaryLifting:
    def __init__(self, edges: List[List[int]], s: List[int]):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        depth = [0] * n
        pa = [[-1] * n for _ in range(m)]
        tin = [0] * n  # DFS 时间戳
        tout = [0] * n
        clock = 0
        path_xor_from_root = [0] * n  # 从根开始的路径的字母出现次数的奇偶性
        path_xor_from_root[0] = 1 << s[0]

        def dfs(x: int, fa: int) -> None:
            pa[0][x] = fa
            nonlocal clock
            clock += 1
            tin[x] = clock
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    path_xor_from_root[y] = path_xor_from_root[x] ^ (1 << s[y])
                    dfs(y, x)
            tout[x] = clock

        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[i][x]) != -1:
                    pa[i + 1][x] = pa[i][p]

        self.depth = depth
        self.pa = pa
        self.tin = tin
        self.tout = tout
        self.path_xor_from_root = path_xor_from_root

    # 返回 node 的第 k 个祖先节点
    # 如果不存在，返回 -1
    def get_kth_ancestor(self, node: int, k: int) -> int:
        pa = self.pa
        for i in range(k.bit_length()):
            if k >> i & 1:
                node = pa[i][node]
                if node < 0:
                    return -1
        return node

    # 返回 x 和 y 的最近公共祖先
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        pa = self.pa
        for i in range(len(pa) - 1, -1, -1):
            px, py = pa[i][x], pa[i][y]
            if px != py:
                x, y = px, py  # 同时往上跳 2**i 步
        return pa[0][x]


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        ord_a = ord('a')
        t = [ord(ch) - ord_a for ch in s]  # 映射成 [0, 25] 中的整数

        g = LcaBinaryLifting(edges, t)
        tin = g.tin
        tout = g.tout
        path_xor_from_root = g.path_xor_from_root

        f = FenwickTree(n)  # 注意树状数组是异或运算
        ans = []

        for q in queries:
            op, x, y = q.split()
            x = int(x)
            if op[0] == 'u':
                c = ord(y) - ord_a
                val = (1 << t[x]) ^ (1 << c)  # 擦除旧的，换上新的
                t[x] = c
                # 子树 x 全部异或 val，转换成对区间 [tin[x], tout[x]] 的差分更新
                f.update(tin[x], val)
                f.update(tout[x] + 1, val)
            else:
                y = int(y)
                lca = g.get_lca(x, y)
                res = path_xor_from_root[x] ^ path_xor_from_root[y] ^ f.pre(tin[x]) ^ f.pre(tin[y]) ^ (1 << t[lca])
                ans.append(res & (res - 1) == 0)  # 至多一个字母的出现次数是奇数

        return ans
