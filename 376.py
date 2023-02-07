# 這題是要找給定的數字列表中，最長的曲折子序列是多長，也就是要去找斜率正負變換的次數
# 做法就是設定兩個參數 up down 來記錄斜率是上升還是下降，先給兩個參數值為 1，然後開始看看前後數字的大小對比
# 如果是遞增的代表說這邊有個 up，然後就更新up的次數，更新方法是 down + 1，這樣才能確定說自己加的是前面一個的遞減時所遇到的數量
# 反之就是把 up down 互換就可以了

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)
      
# 下面是比較數學的版本
# 先找出斜率，然後再去比正負算變化次數
# 不知道為啥理論上下面這個應該會比上面方法多跑一點，但提交出去的結果沒差多少(上38下40)
      
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1: return 1
        diff = list()
        for i in range(1, nums_len):
            diff.append(nums[i]-nums[i-1])
        count = 1
        prev = -diff[0]
        for i in range(len(diff)):
            if diff[i] == 0:
                continue
            if (diff[i] > 0 and prev > 0) or (diff[i] < 0 and prev < 0):
                continue
            count += 1
            prev = diff[i]
        return count
