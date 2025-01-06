# 這題是給一個只有 0 1 的字串然後每次移動只能對於其中一個 1 往左或往右移動一格，問對於每個位置要將所有 1 都集中過去的話，最少需要幾次的移動
# 做法就是先跑一遍，遇到 1 就先算 1 的數量( one_counts)，然後把開頭數字( start_value) 給加上所在的 index，這裡是代表說我把 1 全部都丟到開頭去需要多少步
# 接下來就是開始逐個位置做移動跟計算，首先開頭就直接加進答案內，因為開頭沒甚麼好說的就是已經在上面的迴圈跑完了
# 接下來就是要確認當下位置是不是 1，是的話就需要做個調整，把 1 計數數量( one_counts) 移動 1 個給 pass_counts 來記錄說我已經經過幾個 1 了
# 而接下來做開頭數字的更新，需要更新兩個部分，一個是現在所持有的 1 的數量，因為往下一個位置做移動的時候，其實原本的字元 1 就少移動 one_counts 步
# 接下來就是考慮經過的 1 數量，因為經過他之後他只會一直給妳增加步數，你在經過的 1 們後面代表說他們要移動過來就是隨著迴圈再跑，每次回圈都要往後 + 1 才可以移動這些經過的 1
# 總計經過了 pass_counts 個 1，所以就是減去 pass_counts


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        L = len(boxes)
        start_value, one_counts, pass_counts = 0, 0, 0
        for idx, number in enumerate(boxes):
            if number == "1":
                start_value += idx
                one_counts += 1
        ans = list()
        for number in boxes:
            ans.append(start_value)
            if number == "1":
                one_counts -= 1
                pass_counts += 1
            start_value = start_value - one_counts + pass_counts
        return ans
