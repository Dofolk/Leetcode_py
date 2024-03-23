# 這題是要把字串變成Z字型的
# 做法就是先宣告等量numRows的空間，然後字串走一遍，依據走到的位置將字元擺放進相對應的空間去
# 透過direction來控制要擺放進哪個空間，看是要正序擺放還是逆序擺放
# 簡單來想的話就是用一個空間 rows 來存各個長度位置的資訊
# 從元序列讀取，第一個寫完之後就把讀取頭往下一個地方移過去，直到最後一個位置再折回來

def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        direction = 1
        current = 0
        
        if numRows == 1: return s

        for char in s:
            rows[current] += char
            if current == 0: direction = 1
            if current == numRows - 1: direction = -1

            current += direction

        output = ''
        for row in rows:
            output += row

        return output
