# 這題是給一個字串 list，然後給一個閉區間的 list，問這些閉區間裡面，有多少個字串是母音開頭跟母音結尾的
# 做法就是先跑一遍字串，做出 prefix sum 的 list 來記錄每個區間有多少個符合需求的字串
# 接下來就是依據區間做數量計算就好，直接 尾 + 1 減 頭，因為在座 prefix 的時候會多捕最一開始的0，所以區間的數字需要調整一下

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        prefix_sum = [0]
        current_value = 0
        
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                current_value += 1
            prefix_sum.append(current_value)
        answer = []
        for left, right in queries:
            answer.append(prefix_sum[right + 1] - prefix_sum[left])
        return answer
