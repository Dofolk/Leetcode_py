# 這題是給一個常數 list arr，跟一個 2D array mat，然後根據 arr 所給的數字對 mat 相對應數字的地方塗顏色，問最少幾部可以塗出一條線(不論行或列)
# 所以就是 arr 給塗顏色的數字順序，去塗 mat 裡面的位置
# 這邊就是先做數字對位置的 map，可以開list分別記錄 row 跟 column，然後再開兩個 list 來分別記錄每個 row 跟 column 現在有幾個位置塗色了
# 接著就是跟著 arr 去跑，先確認當下的 row 跟 column 的累計數字有沒有達標，有的話就可以直接回傳 arr index(也就是步數的部分)
# 沒有達標的話就各加一累計起來後，進下一輪的處理

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        if row == 1 or col == 1:
            return 0
        row_element_count, col_element_count = [0] * row, [0] * col
        value_to_row, value_to_col = [0] * (row * col + 1), [0] * (row * col + 1)
        for i in range(row):
            for j in range(col):
                value_to_row[mat[i][j]] = i
                value_to_col[mat[i][j]] = j
        for steps, paint in enumerate(arr):
            row_idx, col_idx = value_to_row[paint], value_to_col[paint]
            if row_element_count[row_idx] == col - 1 or col_element_count[col_idx] == row - 1:
                return steps
            row_element_count[row_idx] += 1
            col_element_count[col_idx] += 1
