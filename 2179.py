# === Description
# 這題是給兩個 0~n-1 重新排序之後的 list num1, num2，然後要問 good triplet 有幾個
# 這邊的 good triplet (x,y,z) 定義為，0 <= x, y, z <= n-1，而且在兩個給定的 list 中，相對應的 index 也是遞增的
# 也就是說 pos1[x] < pos1[y] < pos1[z] 以及 pos2[x] < pos2[y] < pos2[z]，pos就是把輸入的數字轉成位置
# 
# === Thought ===
# 這題可以知道說不只原本的數值 (x,y,z) 要遞增，連相對應的 index 也要是遞增的，所以在這邊可以先取得相對應 index 的位置來做處理
# 在處理 triplet 的問題中，可以選擇透過移動 y 的值或是位置還確認左右兩邊的數量相乘後，做數量的累計就可以有答案了
# 所以在這邊就來考慮移動中間項可以用什麼方法實做
# 那因為在移動中間項的時候，左邊的數量會隨著中間項的移動而有所改變，這邊就會變成我固定其中一條路線再走，另一邊(左邊數量)則是隨著行動有所改變的 prefix sum
# 這裡的 prefix 指的是隨著行動，左邊的數量會逐漸 +1 直到 n-1，所以每次行動的左邊數量不進相同，是個會浮動的 prefix sum 問題
# 面對一個會浮動的 prefix sum 根固定執行步驟的問題，可以選擇使用 Fenwick Tree 來實現，Fenwick Tree 可以參考上一層的學習筆記
# 透過使用 Fenwick Tree 來動態地遞增及計算左邊序列的 prefix sum，這邊的 prefix sum 就是來記錄目標 index 左邊有多少符合目標的數字
# 接著就可以透過左邊及右邊的數量算出當下 y 移動到的位置可以有多少組合
# 因為這題找的 triplet 沒有限制 xyz 的大小關係，所以這邊的可以著重在 index 的大小順序操作就可以了
# 那給定的數字就可以拿來把 nums1 nums2 之間的 index 做 mapping，index1 <-> values <-> index2
# === Code ===
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size
    
    def update(self, index, delta):
        index += 1
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index) # lowbits(x) = x & (-x)
    
    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & (-index)
        return res
        

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n # the index for each number in nums2
        pos2topos1 = [0] * n # the same number for nums1 and nums2, the index correspond from nums2 to nums1
        # 同數值下 nums2 對應到 nums1 的 index 對應表

        for idx, num2 in enumerate(nums2):
            pos2[num2] = idx
        for idx, num1 in enumerate(nums1):
            pos2topos1[pos2[num1]] = idx # index1 <-> values <-> index2
        
        tree = FenwickTree(n)
        ans = 0
        for pos2 in range(n): #移動 y 的位置，從0開始往後去找
            pos1 = pos2topos1[pos2] #找到相對應的 pos1 的位置
            left = tree.query(pos1) #看看 pos1 左邊有幾個數字
            tree.update(pos1, 1) #更新Fenwick Tree的內容，從 pos1 的位置往 tree root開始+1，代表這邊有1個數字可以被累計
            right = (n - 1 - pos1) - (pos2 - left) #右邊可被計算的數字就是 pos1 右邊的還沒對到index的數量去減掉目前 pos2 左邊有對應到 index 的數量
            ans += left * right
        return ans
