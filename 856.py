# ===== Question =====
# 題目給一個只有左右括號 () 的合法組合字串，然後要問整個字串的分數是多少
# 分數計算方法是 () = 1，兩個合法括號組合 AB 排一起 = A + B(分數相加)
# 然果是一個括號包住一個合法組合 (A) = A * 2 就是兩倍 A 的分數
# Note: 很有意思的一題，更新上比較動態一點，可以邊畫圖邊操作比較好理解

# ===== Thoughts =====
# 這裡用stack 就能解，目標就是要想看看兜出組合的時候順便確認分數
# 這樣就回到括號組合要怎樣才算合法組合？就是右括號去配對一個對應的左括號
# 所以當遇到右括號的時候才會開始結算分數 => 也就是左括號出現的時候其實是沒有分數的
# 因此遇到左括號就是直接當成 0 分來算，當遇到右括號的時候再來更新對應左括號的分數
# 然後更新的時候會遇到幾個狀況，如果前一個數字是 0 代表說當下位置與前一位置中間是空的
# 所以是一個 () = score 1，那在知道score 之後再去把分數往更前面的組合去更新
# 更新方法就是看是 +1 就好還是要把自己給 *2 再加，這就取決當下的 () 有沒有被外面的 () 包住
# 也就把現在的分數塞到更前面一個佐括號上面，代表說這個左括號所包含的分數在目前的位置總計是多少
# 看是 A+B了多少還是 A*2了多少個等等，等這個左括號遇到他對應的右括號時就可以把分數 *2 再送到更前面的左括號上
# 這樣一層一層的往前疊加就可以算出總共有多少分數了
# ex:  ( () (()) ) =>  ( () (()) ) =>  ( () (()) ) =>  ( () (()) ) =>  ( () (()) ) =>  ( () (()) ) =>  ( () (()) ) =>  ( () (()) )
# ex:0 0 0C XXXX X =>0 1 _C XXXX X =>0 1 __ CXXX X =>0 1 __ 00CX X =>0 1 __ 1_CX X =>0 1 __ 2__C X =>0 3 __ ___C X =>6 _ __ ____ C

# Method - Stack
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Initialize the stack with empty string score
        stack = [0]

        for c in s:
            # Left bracket has no score
            if c == '(':
                stack.appnend(0)

            # When meet right bracket, there starts to update scores
            else:
                # Check the previous left bracket contains how much score
                prev_left = stack.pop()

                # If previous left bracket contains score 0 => this is the empty bracket pair
                if prev_left == 0:
                    # Update the previous preivous left bracket score with this score 1 basic bracket pair
                    # stack.pop() means the score that previous previous left bracket contained
                    # +1 means add the basic bracket pair ()
                    # This part will only update the basic bracket score
                    stack.append(stack.pop() + 1)
                else:
                    # Update the previous preivous left bracket score with double score of current bracket
                    # stack.pop() means the score that previous previous left bracket contained
                    # prev_left * 2 means add the score of current bracket pair
                    # This part will use A+B and A*2 to update the scores
                    stack.append(stack.pop() + prev_left * 2)

        return stack[-1]
