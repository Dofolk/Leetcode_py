# 這題是給一個字元列表，然後出現一次的字元就留著，超過一次的就把多的移除並留下次數的字元(舉例: 像是有12個'b'，就整理成'b','1','2')
# 做法就是從後面開始做，用前後對比看需不需要計算數量，需要就計算數量後移除該字元，直到遇到不同字元的時候檢查 count 來看要加怎樣的數字字元進去
# 所以最後會檢查的是原本給定的字元列表，有沒有回傳都沒差

class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        for i in range(len(chars)-1,-1,-1):
            if i and chars[i]==chars[i-1]:
                count += 1
                chars.pop(i)
            else:
                if count>1:
                    for item in str(count)[::-1]:
                        chars.insert(i+1, item)
                    count = 1
