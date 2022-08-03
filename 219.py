class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        count = 0
        for i in nums:
            if i in d:
                v = d.get(i)
                if abs(v-count)<=k:
                    return True
                else:
                    d[i] = count
            else:
                d[i] = count
            
            count += 1
        
        return False
      
# 這題要找在長度限制為 k 的長度中有沒有出現重複的值
# 用到字典來處理，紀錄出現的值以及位置，遇到重複就抓出來更新一遍檢查有沒有距離小於 k
# 最後要記得更新遇到的值最新的位置
