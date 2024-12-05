# 這題是給兩個字串 start 跟 target，字串內只有 L R _ 三個字元，分別代表 可往左移 可往右移 空白位置
# 然後問這樣的規則下有沒有辦法把 start 變得跟 target 一樣
# 首先先把順序不一樣的剔除掉，用 replace() 來做就可以了
# 然後開始從後往前確認位置可不可以，像是在 target 遇到 R，就要去確認 start 的 R 有沒有在 target 的後面
# 把整個都跑遍了就知道是對的了

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        idx1, L = len(start) - 1, len(target)
        # check the order of the letter L and R, it must be same
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        for i in range(L - 1, -1, -1):
            if target[i] == '_': # skip blank
                continue
            # since the order is the same, it can just check is 'R' or 'L'
            if target[i] == 'R':
                while idx1 >= 0: # check start index pointer in the range of index
                    if start[idx1] == '_': # if blank, keep index going
                        idx1 -= 1
                        continue
                    elif idx1 > i: # since target's 'R' can't move, if start's 'R' index is bigger, it can't match by the swap to the right
                        return False
                    else:
                        idx1 -= 1
                        break
            else:
                while idx1 >= 0: # check start index pointer in the range of index
                    if start[idx1] == '_': # if blank, keep index going
                        idx1 -= 1
                        continue
                    elif idx1 < i: # since target's 'L' can't move, if start's 'L' index is smaller, it can't match by the swap to the left
                        return False
                    else:
                        idx1 -= 1
                        break
        return True
