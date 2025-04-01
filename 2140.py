# === Description ===
# 題目會給一個 2 x n 的 2d array，代表著 [分數, 跳過次數]，對於每個位置可以決定要不要拿分數
# 拿了分數的話往後跳過次數的分數都不能拿，如果不拿分數的話就移到下一個位置在做一次拿不拿分的選擇
# 問所有位置都跑過之後，最多可以拿幾分

# === Thought ===
# 這是個 DP 問題
# 正面從頭去算題目的話，可以想成說我當下的數字就是我目前位置往前所可以得到最好的數字
# 接著往後去更新數字，首先更新 idx 沒有選擇的狀況下，我後一個位置(idx + 1)就去跟 idx 比誰大就更新
# 接下來是 idx 有選擇時，當下位置(idx)加上選擇得分以及下一個位置(later = idx + 跳過次數 + 1)本身數字哪個大
# later 的數字有可能就是其他位置(非idx)剛好可以更新到 later 來，這樣就可以去比較哪個位置可以拿到最大的數字
# 如果 later 超過最大上限的話，就照最大上限來算，因為前面的大數字都還是會累積到最後一個位置
# 所以這樣一直更新到最後就可以得到最後累積的結果了
# 反面想的話也是同理，指示由後往前去累積，當下位置(idx)如果沒有後面位置(later = idx + 跳過次數 + 1) 可以累積
# 就直接把 idx + 1 往前遞補，跟正面來的不選擇是一樣的

# === Code ===

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        L = len(questions)
        record = [0] * L
        prev = questions[-1][0]
        
        for idx in range(L - 1, -1, -1):
            record[idx] = prev
            val, dis = questions[idx]
            later = idx + dis + 1
            if later < L:
                val += record[later]
            if val > prev:
                record[idx] = val
            prev = record[idx]
        return record[0]
