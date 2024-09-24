# 這個問題會給一個常數列表，目標是要找說每個位置的左手邊，數值小於當前位置的數字及距離最近的值是多少
# 想法就是我先去比對前一個位置的數字大小，比較大的話最近的一定就是面前的這個
# 比較小的話我就可以去跟前一個數字的 nearest smaller element(NSE)去比較，因為這個就是前面一個的最近較少的數字了，所以跟他比較就可以了
# 跟NSE比的時候，當下數字小於NSE的話就代表還要再往前去看更前面的數字是多少，因為明顯的當下數字就更小一些
# 當下數字比NSE大的時候就代表說已經找到再往前一點的最近較小的值了
# 實作方法可以用stack來記錄說前面的NSE有哪些，且可以不重複紀錄，以減少計算時間
# 等真的stack裡面都找不到更小的數字的時候就代表說我當下的數字真的是目前與到最小的數字，就在result裡面添進-1
# 最後再把當下的數字放進stack裡面，因為下次的比較就會需要用到的"下一步的前面的數字"


def near(arr):
    res = []
    stack = []
    for val in arr:
        while stack and stack[-1] >= val:
            stack.pop()
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(val)
    
    return res
