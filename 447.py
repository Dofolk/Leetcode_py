# 這題是給一堆點，然後算出有多少組可以做到一點為圓心然後其餘兩點為相同半徑
# 做法就是直接暴力解，所有的點都跑一遍，用字典來記錄

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        
        for a, b in points:
            counter = {}
            for x, y in points:
                dist = (x - a)**2 + (y - b)**2
                if dist in counter:
                    count += 2*counter[dist]
                    counter[dist] += 1
                else:
                    counter[dist] = 1
        
        return count
            
