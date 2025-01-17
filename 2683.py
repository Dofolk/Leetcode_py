# 這題是給一個只有 0 1 的 list(derived)，然後說這個 list，對於位置 i 是由另一個 0 1 list(source) 的 i XOR i + 1 來的，最後一個就往頭循環回去做 XOR
# 就問說，這個另一個 0 1 list 有沒有存在
# ex: [1, 0]就不存在能產生他的 xor list，[1, 1]就可以用 [0, 0] 或 [1, 1] 做出來
# 作法也是簡單，就是算 1 的數量是不是偶數就好
# 原理是 derived 裡面所有的數字做 XOR 的概念就是把 source 所有識字給 XOR 兩次，這樣看的話就知道第一個做法，把所有 derived 的元素做 xor 要 = 0
# 接著就是把 0 拉進來想，如果 1 的數量不是偶數的話，做出來的最後結果會是 1，就跟上面的結論不合，所以檢查 1 的數量奇偶就可以了

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return not sum(derived) % 2
