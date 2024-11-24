# 這題是問說有個 m x n 的盒子，裡面有石頭、固定平台跟空的地方，現在把盒子向右轉 90 度，石頭會掉到哪裡，長什麼樣子
# 想法就是轉 90 度之後最底層就是旋轉前最右邊，所以做的時候就是從最尾端往前，找看看哪邊是平台，哪邊可以讓東西掉下來
# 所以設定一個 pos 來記錄目前可以存放東西的位置，然後遇到平台的話就更新 pos 為往前一格的位置
# 然後遇到石頭就把 pos 跟石頭做交換就可以了

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        for row in box:
            pos = len(row) - 1
            for idx in range(len(row) - 1, -1, -1):
                if row[idx] == "*":
                    pos = idx - 1
                if row[idx] == "#":
                    row[idx], row[pos] = row[pos], row[idx]
                    pos -= 1
        
        return zip(*box[::-1])
