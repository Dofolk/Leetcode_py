# 這題是要看電話上面的英文字母可以組成多少組合並列出來
# 給定一串數字，看看相對應的英文字母可以有多少組合
# 作法有幾種，一是暴力解，二是用遞回，三是backtrack
# 暴力解就沒甚麼好說的，直接巢狀刻好就可以了
# 遞迴的話就是確認是不是最後一個數字，是的話就抓對應的英文字回傳，回傳到上一個層級去做組合
  # 如果不是最後一個字的話就往下 call 後面的組合出來，再用一個 double for 來做組合
# 最後一個是 backtrack，有點像是在做 tree 的建立且也是用遞迴操作，先握好前面數字得到的第一個英文字母，然後往下再加一個後面數字得到的第一個英文字母
  # 等遇到最後的數字時就把手上握著的所有字母組合並儲存，然後丟掉最後一個得到的字母，改成握最後數字的次一個字母
  # 等到最後一個數字的字母都完成儲存之後就往回找倒數第二個數字的第二個字母，再往下去拿最後數字的第一個字母，重複做上一行的事情
  # 最後就可以建構出所有的東西了

# 1 (可以在修改一下，很多不必要東西，像是D改成全字串，不用轉換常數等等的)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        D = {2:['a','b','c'],
             3:['d','e','f'],
             4:['g','h','i'],
             5:['j','k','l'],
             6:['m','n','o'],
             7:['p','q','r','s'],
             8:['t','u','v'],
             9:['w','x','y','z']}
        if len(digits) == 1: return D[int(digits)]
        
        ans = list()
        digits = list(digits)
        for i in range(len(digits)):
            digits[i] = int(digits[i])
        
        for i in D[digits[0]]:
            for j in D[digits[1]]:
                if len(digits)>=3:
                    for k in D[digits[2]]:
                        if len(digits)==4:
                            for l in D[digits[3]]:
                                ans.append(i+j+k+l)
                        else:
                            ans.append(i+j+k)
                else:
                    ans.append(i+j)
        
        return ans
# 2
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def dfs(digits, ind):
            if ind == len(digits)-1:
                current_combo = phone.get(digits[ind])
                combos = []
                for c in current_combo:
                    combos.append(c)
                return combos
            
            next_combos = dfs(digits,ind+1)
            current_combo = phone.get(digits[ind])
            combos = []
            
            for c in current_combo:
                for n in next_combos:
                    combos.append(c+n)
            return combos
        
        return dfs(digits,0)

# 3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        combination = []
        def backtrack(index, path):
            if len(path) == len(digits):
                combination.append("".join(path))
                return
            
            current_letter = phone.get(digits[index])
            for i in current_letter:
                path.append(i)
                backtrack(index+1,path)
                path.pop()
            
        backtrack(0,[])
        return combination
            
