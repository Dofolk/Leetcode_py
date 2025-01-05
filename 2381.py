# 這題是給一個字串跟一堆區間要往前或往後移動一個位置(b->a or b->c)，問經過這些區間的移動之後，字串變成怎樣？
# 做法就是去紀錄區間的頭尾是要增加還是減少，依據方向來決定投的部份是要增加或減少，這部分問題不大
# 接著就是去看看區間偉的後面還有沒有空間，要來記錄從這邊之後，這個區間頭所帶來的影響要復歸
# 意思就是，我在區間頭時是要往前移動一格，那我就錄在頭 +1，這樣我後面再跑字串的時候只需要在頭的地方 +1 並且保持這個識字往下去就可以做到區間內的字元移動
# 但是超過區間怎麼辦？我就給他 -1 扣回來，這樣在區間外的移動就又變回 0，而保持不變
# 這就是去指定頭要去增減，然後尾端去做復歸平衡的做法
# 最後再依據需要增減的數量就可以找出所有移動後的字元並湊成字串
# Ex: s = "abcd", shifts = [[1,2,1]]，這代表說我的 "bc" 要變成 "cd"
# 這邊就會記錄到說我有個差距長 diffs = [0, 1, 0, -1]，接著在重頭跑一遍字串時，最一開始 shift_count = 0，因為一開始沒有任何增減
# 接下來，在 position 0 的時候 shift_counts += 0，所以 a 不變，然後遇到 1 就把 shift_counts += 1，所以就變成 1，把 b 變成 c
# 然後再這個區間內 position 2 的部分也因為前面的 shift_count = 1 加上自身 +0，所以把 c 變成 d
# 最後因為我原本的 d 不再區機內不能增減，所以要在 diffs 最後的位置打上 -1，這樣跑到這裡時，我的 shift_counts 就被扣回來 0
# 這樣就可以完成這個區間的移動復歸
# 接著讓更多的區間加進來，讓頭尾的位置做出增減，一切都統計好之後從頭跑一次字串就完成了

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        L = len(s)
        diffs = [0] * L
        for left, right, direction in shifts:
            if direction:
                diffs[left] += 1
                if right + 1 < L:
                    diffs[right + 1] -= 1
            else:
                diffs[left] -= 1
                if right + 1 < L:
                    diffs[right + 1] += 1
        
        result = list(s)
        shift_counts = 0

        for idx in range(L):
            shift_counts = (shift_counts + diffs[idx]) % 26
            shift_char = chr( (ord(s[idx]) - ord('a') + shift_counts) % 26 + ord('a') )
            result[idx] = shift_char
        return ''.join(result)
