# 這題是要把數字串變成口語化字串，看到"1"的時候我們會說 '1'個'1'，所以'1'就會變成'11'
# 這題的做法就是用類似 two pointer的概念去做，不過會需要宣告一個全域變數來存目前的字串長怎樣
# two pointer 的部分就是一個用來定位置(j)，一個用來算數量(k)，當遇到不同數字時就更新 next_str，給他加上 k-j(數量)+第j個數字
# 最後再把j移動到k的位置，完成一個數字的數量字串的更新

class Solution:
    def countAndSay(self, n: int) -> str:
        current_string = '1'
        for _ in range(n-1):
            next_str = ''
            j = 0
            k = 0
            while j < len(current_string):
                while k < len(current_string) and current_string[k] == current_string[j]:
                    k += 1
                
                next_str += str(k-j) + current_string[j]
                j = k
            current_string = next_str
        
        return current_string
