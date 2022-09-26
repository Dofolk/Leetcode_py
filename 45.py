# 這題是給一串數字，每個數字代表在那個地方當起點時可以最多往後走幾步，找看看走到最後最少的步數
# 貪婪演算法的題目，首先在走的時候就會知道說我這一步能跨多遠，所以就形成一個上一步的跨越區(current_jump_end)
# 然後就開始在上一步的跨越區裡面找下一步要在哪邊走可以走到最遠，隨時更新 farthest 的數字
# 最後走到上一步跨越區的盡頭時就可以更新一下最遠走到哪邊去，也更新了下一次的上一步跨越區能走到哪邊去更新

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        
        return jumps
