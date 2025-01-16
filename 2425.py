# 這題是給兩個常數 list，然後對於兩個 list 所有的元素都做 pair 後做 XOR，等所有 pair 都做完之後把所有結果都做 XOR，問最後的 XOR 數值是多少
# 這題可以先想一下 XOR 的性質， a XOR a = 0，所以這樣的性質可以先做一個篩選，如果知道有元素會去做偶數個 pair 時，到最後的 XOR 會發現這個元素會直接為 0
# 所以這邊就可以用長度來看看有哪些數字需要做的，如果另一條長度是偶數，那就自己所有數字都不用跑，因為這邊的所有數字都會出現偶數字，會 = 0
# 如果是奇數，那就所有數字跑一遍就可以了
# XOR 還有個性質可以使用，就是 a XOR 0 = a，這個讓 ans 最一開始設定的時候當成 0 就好

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        L1, L2 = len(nums1) % 2, len(nums2) % 2
        if not L1 and not L2:
            return 0
        ans = 0
        if L2:
            for num in nums1:
                ans ^= num
        if L1:
            for num in nums2:
                ans ^= num
        return ans
