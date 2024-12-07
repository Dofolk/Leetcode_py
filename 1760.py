# 這題是給一個數字 list 跟最大操作次數 maxOperations，每次操作時可以將一個數字分解成兩個更小的數字相加(都要>0)
# 在有限次數的情況下，將最大值盡可能的降到可能的最小，這樣該值是多少
# 想法就是把 binary search 套用在尋找中間值，然後我們每操作一次就會多一個空間出來(ex. 5->2+3，一個5變成兩個數字)
# 所以最後總共會有 len(list) + maxOperations 這麼多的位置(全域)可以放東西，這樣的想法方便我們比較精準的定位出 binary search 的 low 跟 high
# low 定成家總的全域平均值，因為最大的數字不管怎麼切，在有限空間的狀況下一定不會小於平均值
# 接著把 high 定成當前最大值以及加總除操作次數，這邊要不就是從最大值開始往下找，要不就是一個很大的值去切分(像是一個超大數平均切成 n 等分還比其他數字大，[1,1,100] 2，100/2 = 50 >1)
# 接著開始二分尋找中間值，確認操作次數有沒有超過限制，更新 low high 的數值，直到最後回傳 high 就可以了
# 在確認的時候，做 x - 1 // middle value 來確認操作次數，因為 a * middle value + residual(<middle value) 需要拆分的次數是 a - 1 次，但是當 residual 大了那麼一點點(1)，你就會需要多一次
# 反過來說也就是你需要的拆分次數，就是將多出來的那麼一點點給減掉在去 mod middle value 就對了
# Ex. 9->3+3+3, 2次拆分, mod 是 3, 所以9其實是跟 7, 8 同一掛的；10->3+3+3+1, 3次拆分, mod 是 3
# 123,456,789,...，所以判斷的時候要注意

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        S = sum(nums)
        total = len(nums) + maxOperations
        if total >= S:
            return 1
        low = math.ceil(S/total) - 1
        high = min(max(nums), math.floor(S/maxOperations))
        while low < high:
            mid = (low + high) // 2
            if sum( (i - 1) // mid for i in nums) <= maxOperations:
                high = mid
            else:
                low = mid + 1
        return high
