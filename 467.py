# 這題是給一個字串 s 去構成重複的無限長度字串，然後去找他的唯一子字串
  # 這邊定義一下要找的東西是什麼，要符合以下條件:
  # 1. 必須是字串位置上是連續的子字串，也就是說在原本 index 看來是連續的，像是 abc 中 bc 就是一個子字串而 ac 就是
  # 2. 必須是字母順序上是連續的，也就是要按照 abcd...xyz 的順序，然後因為是無限迴圈的樣子所以在給的 s 裡面出現 zabc.. 也算是有按照順序
  # 3. 必須是唯一的，像是給了 s = 'abab' 的話會先後各遇到一個 'ab'，這時候只計算前面最先遇到的那一次
  # 其中第二點比較重要，因為在數學上認知的 substring 跟這裡的不太一樣意思.....
# 想法就是從給定的 s 裡面去找每個字元開頭能找到多長的子字串，每找一次就在結果加上一次
# 這時候就要借助一個額外的 count 來記錄目前每個字母開頭的時候最長的長度，以免重複計算
  # 因為像是 'ab' 可以有 'a' 'b' 'ab' 三種狀況，在 'a'開頭的時候會先算一次長度為 1 的 'a' 後面再去加兩個 'b' 'ab'
  # 如果現在變成 'ababc' 的話，在前面已經算過 'ab' 的所有可能性了，所以後面遇到 'ab' 時就會先暫時不加算結果，等到真的從 'ab' 變成 'abc'的時候再去加算

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        count = [0]*26
        res, L = 0, 0
        for i in range(len(s)):
            cur = ord(s[i]) - ord('a')
            if i > 0 and ord(s[i - 1]) != (cur - 1) % 26 + ord('a'):
                L = 0
            L += 1
            if L > count[cur]:
                res += L - count[cur]
                count[cur] = L
        return res
