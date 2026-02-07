"""
題目是說給一個只有 a b 的字串，移除最少的字元，使得移除後的結果形成aaa....abbb..bb，先a後b的字串
keypoints: a 前面不能有 b，所以可以算b的數量並且步進，來看看走完一趟能不能把b給消耗完，或是a不夠多只好把a移除掉來取得最小移除次數
"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        '''
        Greedy算法
        在a之前不能有b出現，所以每次遇到a的時候就知道一定會有一個字元被移除
        這個字元不管是移除當下的a或是前面的b都好
        所以這邊就去記錄當下的a前面有幾個b，遇到b就累計
        遇到a就看看前面有沒有b需要移除，當遇到比較多b的時候這個做法可以想成是把這些短短的a做移除
        因為你只會更新a遇到的次數
        for ex: aaabbbbaab在後面那段aa的時候只有更新兩次，但前面的b還沒消耗完
        所以這邊就變成是移除a的次數，因為當b_count真的被移除完之後又遇到a的時候是不會去做更新
        代表a的數量就是比較多，我去移除b比較划算
        '''
        res, b_count = 0, 0

        for char in s:
            if char == 'b':
                b_count += 1
            elif b_count:
                res += 1
                b_count -= 1
        
        return res
