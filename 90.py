# 這題是要找 subset，然後會有重複的值
# 做法就是用 set 來做處理，宣告一個 set 來做紀錄，然後就用 double for 來做，把新的元素逐個加入到目前所有的子集合裡之後加進去res裡
# 最後在把成果弄成 list 就可以輸出了

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = {()}
        for num in sorted(nums):
            for item in res.copy():
                res.add(tuple(list(item)+[num]))
        return [list(item) for item in res]
