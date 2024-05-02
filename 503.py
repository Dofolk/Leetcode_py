# 這題是把一常數序列當成環狀的，所以最後一個數字的下一個就是開頭的數字，問題是對於每一個數字來說，它的往後的第一個 比較大的數字是多少
# 想法是因為要找比較大的樹，所以可以考慮 monotonic stack 來做數字的大小排序
# 因為這邊的序列是會循環的，所以就先多做一次來找最後面那些會跑到重複序列的位置
# 再加上重複一次及 mod 的想法，所以在跑重複位置的時候就是用 % 來控制位置
# 結果整個流程變成：先訂好基本需要的參數，for 跑 2n-1 次來當成循環一次要找的地方，然後從最後一個網前來做monotonic stack
# 接著就是每步都確認循環多出來的那部分n 都有沒有跑過了，就可以有一個 stack 存數字讓最基本的序列來找數字
# 最後把數字再推回 stack 裡面

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        L = len(nums)
        stack = list()
        res = [-1] * L
        for i in range(2*L - 1, -1, -1):
            while stack and stack[-1] <= nums[i%L]:
                stack.pop()
            if i < L and stack:
                res[i] = stack[-1]
            stack.append(nums[i%L])
        return res
