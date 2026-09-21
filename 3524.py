# ===== Question =====
# 題目給一個正整數列表 nums 跟一個正整數 k，然後要回傳一個長度為 k 的結果 res
# 你可以對這個 nums 的任意長度 prefix 和任意長度 suffix 做移除，但移除後不能是 empty
# 接著把所有留下來的數字乘積起來之後去 mod k 後取得餘數 q，然後這樣就是算餘數 q 的一種組合
# 現在把所有的組合都確認過回傳 res

# ===== Thoughts =====
# 針對題目的敘述，可以把題目轉換成現在要找所有的 sub array 來計算他們的餘數 q
# 可以這樣轉換的原因就是移除 prefix suffix 就會剩下一段連續的 sub array
# 所以一個sub array 都會有一個對應的 prefix suffix 被移除
# 這樣煮患之後題目就變成一個經典的 dp 問題，掃過所有的位置來確保所有 sub array 都有被計算到
# => 位置 idx 的狀態可以由位置 idx - 1 的狀態演變而來(反過來也可以)
# 這邊的 DP 是開一個 len(nums) * k 大小的陣列做紀錄，但因為每一次都只有跟前一次有關，所以可以做 rolling DP
# 這裡就用 res 紀錄最終結果，freq 記錄前一次 (idx - 1) 的結果，curr 記錄當下位置 (idx) 的結果
# res 跟 freq 初始化可以直接全是 0 因為啥都沒有，curr 的話就把當下的餘數算成 1，因為最少就會有自己留著
# 演進的方式就是前一次餘數 q 有 freq[q] 個組合，現在 q 乘上 nums[idx] % k 取得當下的餘數 q_idx
# 這 freq[q] 個組合就可以推進到 q_idx 的組合裡面，然後再把 freq 累進至 res 裡面就可以了

# Method - DP
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return [n * (n + 1) // 2]
        nums = [num % k for num in nums]
        if k == 2:
            groups = groupby(nums)
            counts = [len(list(group)) for key, group in groups if key != 0]
            odds = sum(count * (count + 1) for count in counts) // 2
            return [(n * (n + 1)) // 2 - odds, odds]
        
        res = freq = [0] * k
        
        for num in nums:
            # num %= k
            curr = [0] * k
            curr[num] = 1
            
            for val, f in enumerate(freq):
                curr[val * num % k] += f
            
            freq = curr
            for val, f in enumerate(freq):
                res[val] += f
        
        return res
