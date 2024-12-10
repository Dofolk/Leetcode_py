# 這題是給一個字串，然後說字串是特別的時就是連續同字母產生的子字串，然後問在字串中，連續出現三次以上的特別子字串，最長的長度是多少
# 首先先找到每個字母拼成特別字串的長度是多少，並且記錄下來
# 接著就可以對長度做篩選及取用，首先對最長的子字串看看有沒有超過2，因為超過的話就可以算第一次的長度了 aaa -> a, aaaa -> aa since aaaa = aa,aa + a,aa,a + a,a,aa所以最長是aa出現3次
# 然後再來看看這個字母有沒有出現過很多次，有超過 2 次的話可以來考慮次長的子字串，這樣可以找出最常跟次長的子字串可以湊出多長的子字串，因為有重複三次的問題，所以需要找 最長 - 1 跟次長的最小值來當最大值的比較
# 如果最長次長都是5，這樣只能有4的長度(在不知道地3個是否為5的狀態下)，如果最長是5次長<5，那這樣在出現3次的限制下，次長的長度就是目前可以取得最長的長度，沒辦法用最長(因沒辦法出現3次)
# 最後就是如果長度超過 3，就是可以再去多考慮第三長的長度了，因為有跟次長的比較過了，所以在第三長的直接做簡單的最大對比就可以了，因為都到第三了，要不前面一輪拿到比3rd還大，要不就是3rd最長了

class Solution:
    def maximumLength(self, s: str) -> int:
        cnt_dict = defaultdict(list)
        cnt = 0 # count the length of subsequnce with same alphabet
        current_c = None # record the previous alphabet
        s = s + "1" # add an end
        for c in s:
            if not current_c:
                current_c = c # reset previous alphabet
            if current_c == c:
                cnt += 1
            else:
                cnt_dict[current_c].append(cnt) # record the length of the special substring
                current_c = c # reset previous alphabet
                cnt = 1 # reset count numbers
        ans = -1
        for k, v in cnt_dict.items():
            v = sorted(v, reverse=True) # sort out the longest length of the special substring
            if v[0] > 2: # by the limitation that needs show up for at least 3 times
                ans = max(v[0]-2, ans)
            if len(v) >= 2 and v[0] > 1:
                ans = max(min(v[0]-1, v[1]), ans)
            if len(v) >= 3:
                ans = max(ans, v[2])

        return ans
