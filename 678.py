# ===== Question =====
# 題目給一個只有左右括號 () 以及星號 * 的字串，然後星號可以是 '(', ')' 或 '' 空字元
# 問能不能組成一個合法的 () 字串

# ===== Thoughts =====
# 組成合法 () 的時候可以考慮用 stack 來操作，再加上這題有星號這個好用的彈性空間
# 所以考慮分別對左右括號各自做組合處理，先把右括號跟左括號配對並且計算消耗的星號
# 接著就是把沒有配對的左括號跟星號做處理
# 整個流程就是：首先用一個 stack 用來存左括號的位置、一個 star_pos 用來存星號的位置
# 第一步處理位置紀錄以及右括號的配對，右括號先消耗左括號的紀錄，再去考慮消耗星號
# 因為星號萬用，所以配對的消耗優先程度來說左括號能用完就先用完
# 如果左括號跟星號都沒有了的話就可以提早回傳 False，因為到這邊一定就沒辦法做出合理的括號組了
# 第二步在處理完現有的右括號之後，就剩下左括號跟星號要接著處理
# 這邊就是去檢查最右邊的左括號跟最右邊的星號位置(stack[-1] <--> star_pos[-1])
# 如果左括號比星號還前面的話就消耗掉星號；如果位置比較後面就停止，代表我現在要處理的左括號沒有星號可以湊對
# 最後就是還傳左括號還有沒有剩

# Method - Stack
class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[0] == ')' or s[-1] == '(':
            return False
        
        stack = []
        star_pos = deque([])

        for idx, c in enumerate(s):
            if c == '(':
                stack.append(idx)
            elif c == '*':
                star_pos.append(idx)
            else:
                if stack:
                    stack.pop()
                elif star_pos:
                    star_pos.popleft()
                else:
                    return False
        
        if len(stack) > len(star_pos):
            return False
        
        while stack and star_pos:
            if stack[-1] >= star_pos[-1]:
                break
            stack.pop()
            star_pos.pop()
        
        return not stack
