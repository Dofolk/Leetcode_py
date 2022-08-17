# 這題是要找給定的序列中第三大的數字，重複不計。如果沒有第三大的話就回傳最大的那個
# 做法就是先排序，然後用一個 list 紀錄最大的數字們，一碰到長度3的話就 pop 收工，沒有的話就繼續找繼續添加
# 最後還要有一個判斷是有可能剛好3個為一串，沒辦法在 for 裡面跳出來，最後加一個判斷式來確認最終長度跟要輸出的值

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        l = []
        for i in nums:
            if len(l) == 3:
                return l.pop()
            elif i not in l:
                l.append(i)
            
        if len(l) < 3:
            return nums[0]
        if len(l) == 3:
            return l.pop()
