# 這題是給一個只有abc的字串跟一個數字 k，每次選擇只能從最左邊或最右邊挑一個拿著，讓自己拿著的abc各數量最少要k個，問最少拿多"少"次可以達成目標
# 想法就是用 sliding window，加上類似two pointer的想法，讓一個指標往前進，扣除當下指標字母的數量，接著去確認看看這個字母要不要扣
# 以這種作法去拉出一個two pointer的寬度，代表說有這麼長的字母是不需要的，最後再去用總長度減右加左再減一(要補一下才計算的出正確長度)

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = [0] * 3
        size = len(s)
        
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        if freq[0] < k or freq[1] < k or freq[2] < k:
            return -1
        
        left = right = 0

        for right in range(size):
            freq[ord(s[right]) - ord('a')] -= 1

            if freq[0] < k or freq[1] < k or freq[2] < k:
                freq[ord(s[left]) - ord('a')] += 1
                left += 1
        
        return size - right + left - 1
