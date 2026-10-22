# ===== Question =====
# 題目會給一個只有小寫字母的字串 s，然後每次只能取一個連續子字串做排序
# 這個子字串不能是 s 本身，這樣的限制下，最小做幾次可以讓整個 s 遞增排序 a->z

# ===== Thoughts =====
# 最有效益的曲子字串方法就是少一個字母的字字串做排序，因為這是能娶到最大的長的子字串了
# 這樣取的時候要不去頭要不去尾，所以頭尾的字母就變得重要了，也就是本題關鍵所在
# 所以要考慮的就是 頭尾倆的位置 跟 字串最大 M 字串最小 m 之間的關係
# 首先先做一些簡單排除，像是本來就遞增或是長度為二但遞減(沒辦法交換)的狀況
# 接著就是去看大小關係(在各行註解))

# Method - Check Relationship of max/min with left/right end node
class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 2 and s[0] > s[1]:
                return -1
        
        for c1, c2 in pairwise(s):
            if c1 > c2:
                break
        else:
            return 0

        M, m = max(s[1:-1]), min(s[1:-1])
        left, right = s[0], s[-1]
        # 左邊是整個字串最小或是右邊是整個字串最大，只需要做一次就好
        if left <= min(m, right) or right >= max(M, left):
            return 1
        # 如果在中間區段有最大或最小的時候就做兩次就可以了，這邊就確認右邊>=中間最小或是左邊<=中間最大
        elif right >= m or left <= M:
            return 2
        # 剩下的就是左邊最大且右邊最小，然後中間區段還沒有最大或最小
        else:
            return 3
