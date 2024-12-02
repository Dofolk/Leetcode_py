# 這題是問說能不能在 list 裡面找到兩個數值 a, b 使得 a = b * 2，可以的話就回傳 True，否則 False
# 這個做法比較簡單，可以用 set() 來當 hashtable，紀錄有遇到過的數字，然後再遍尋所有數值的時候，去檢查該數字 * 2 或是 / 2 有沒有在 set 裡面遇到過
# 像是先遇到 5 後有 10，因為先遇到，所以 5 已經在 set 裡了，這時候讓 10 來判斷乘 2 的 20 及除 2 的 5 有沒有遇到過
# 有的話就可以回傳 True 了

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        S = set()
        for i in arr:
            if i * 2 in S or i / 2 in S:
                return True
            else:
                S.add(i)
        return False
