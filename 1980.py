# 這題是給一個只含 01 且長度為 n 的字串列表 nums ，同時列表的長度也為 n，問說這樣的列表裡面，哪個長度 n 的 01 字串沒有出現過，如果有多個，回傳任一個就好
# 因為只有 01 所以可以用二進位來思考，再加上 n 有限制最多是 16，所以其實就是從 0 ~ 16 去找沒出現過的數字就好
# 這邊可以先用一個 list 來記錄 nums 裡面有幾個數字出現過，再從列表裡面把第一個遇到的沒出現過的數字回傳就好

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        m = min(len(nums) + 1, 17)
        record = [0 for _ in range(m)]
        for num in nums:
            if int(num, 2) < m:
                record[int(num, 2)] = 1
        for idx in range(m):
            if record[idx] == 0:
                return format(idx, 'b').zfill(len(nums))
