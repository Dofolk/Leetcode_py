# 這題是給兩格字串的 list，然後問說第一個字串 list 裡面有哪些字串，可以包含 list 2 的所有字串
# 也就是說 list 2 裡面的字串都是該字串的 subset，不需要考慮連續性的那種
# 這題的做法就是先把 list 2 裡面所有的需求先開好，像是哪個字元最多要有幾個
# 接下來就是去 list 1 裡面逐個字串去對需求，沒有符合需求的舊移除掉，合規的就留著等回傳
# 這邊再移除的時候可以使用 set 來加速

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_nums = defaultdict(int)
        seen_word2 = set()
        for word in words2:
            if word in seen_word2:
                continue
            for char in word:
                char_nums = word.count(char)
                if char_nums > max_nums[char]:
                    max_nums[char] = char_nums
            seen_word2.add(word)    
        
        ans = set(words1)
        for word in words1:
            for char in max_nums:
                if max_nums[char] > word.count(char):
                    ans.remove(word)
                    break
        return list(ans)
