# 這題是要找最長的非相似子序列是多長，所以想法就是找最長的唯一樣式子序列(可以等長但不能字都相同)
# 因為最長的子序列就是自己本身，所以再找的時候就是以最長的那個序列開始找，先做整個list的長度遞減排序
# 然後用一個判斷函示來判斷說目前的序列是不是前一或幾個序列的子序列，然後一個一個跑過去
# 因為是遞減的，所以只要有其中一個都找不到一樣的序列十，就可以回傳了，因為後面得長度都 <= 當下的

# Sol 1
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSub(w1, w2):
            # 簡單的長度比對後回傳
            if len(w1) > len(w2):
                return False
            # 來看看是不是子序列，以後序列來對比前序列，這邊主要處理的是後序列長度=前序列
            i = 0
            for s in w2:
                if i < len(w1) and w1[i] == s:
                    i += 1
            # 最後回傳有沒有跟前序列一樣的長度
            return i == len(w1)
        # 以長度做遞減排序
        strs.sort(reverse = True, key = len)
        L = len(strs)
        # 從頭開始一個字一個字找
        for i, word1 in enumerate(strs):
            # found 的意思指的是現在的 word 1 找到跟他一樣的字串序列，所以一開始設定是 False 來表示還沒找到
            found = False
            for j in range(L):
                if i!=j and isSub(word1, strs[j]):
                    found = True
                    break
            if not found:
                return len(word1)
               
        return -1

# Sol 2
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSub(w1, w2):
            if len(w1) > len(w2):
                return False
            
            i = 0
            for s in w2:
                if i < len(w1) and w1[i] == s:
                    i += 1
            
            return i == len(w1)
        
        strs.sort(reverse = True, key = len)
        for i, word1 in enumerate(strs):
            # 這邊直接縮起來寫，然後用 all() 來跑所有的可能
            if all(not isSub(word1, word2) for j,word2 in enumerate(strs) if i != j):
                return len(word1)
        
        return -1
