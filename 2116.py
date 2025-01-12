# 這題是給一個含有 "(" 跟 ")" 的字串，以及對於每個位置有無鎖定的 01 字串，未鎖定的位置可以任意更改左右括號
# 問給定的這些東西能不能組合出合法的括號關係
# 這題要先知道第一個麻煩的東西就是 "1"，因為你這個位置就不能更動了，所以需要做合法的配對處理
# 所以第一次跑一遍的時候，遇到 0 的時候就記錄下當下的位置，當不是 0 的時候就確認是 "(" 還是 ")"
# 如果是 "("就得既ˋ錄起來，因為我不知道後面能不能湊出合法的配對，如果是 "(" 的話先確認一下前面有沒有 "("，可以湊成一對減少麻煩的數量
# 如果真沒有不能更動的 "(" 時就只能乖乖地拿可任意變動的位置來用
# 跑一遍之後就可以確認說我剩下沒辦法配對的 "(" 在哪些地方，接著就去檢查 "(" 最後出現的位置在哪裡
# 如果最後出現的位置後面宅有可任意變動的扣打時，我就可以做出配對
# 一直跑到 "(" 的位置沒有了，或是最後的 "(" 位置後面已經沒有扣打能用
# 最後的最後，檢查一下 "(" 有沒有都配對完就可以回傳結果ㄌ

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        L = len(s)
        if L % 2 or (s[0] == ")" and locked[0] == '1') or (s[-1] == "(" and locked[-1] == '1'):
            return False
        unlocked = []
        left = []

        for idx in range(L):
            if locked[idx] == "0":
                unlocked.append(idx)
            elif s[idx] == "(":
                left.append(idx)
            elif s[idx] == ")":
                if left:
                    left.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        
        while left and unlocked and unlocked[-1] > left[-1]:
            left.pop()
            unlocked.pop()
        
        return True if not left else False
