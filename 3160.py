# 這題是給一堆球跟顏色，現在給一個 queries 代表要對球刷上某個顏色，問每個步驟之後，球的顏色有幾種
# 做法就是用一個 ball_color 紀錄求目前的顏色， color_count 來記錄顏色出現的次數，以及 total_count 來記錄目前有幾種顏色
# 接著就是按照步驟進行，先確認球有沒有刷過色，有的話就進行換色跟把 color_count 減少及確認顏色還存不存在(如果count = 0 代表該顏色最後一顆球被覆蓋掉了，顏色就不見了)
# 接著就把球的顏色給換好，最後把顏色出現次數做更新，沒出現過的顏色就建起來並且把總顏色數量 +1 ，然後就可以存該步驟的顏色總量了

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = dict()
        color_count = dict()
        total_count = 0
        ans = list()
        for ball, color in queries:
            if ball in ball_color:
                org_color = ball_color[ball]
                color_count[org_color] -= 1
                if color_count[org_color] == 0:
                    color_count.pop(org_color)
                    total_count -= 1
            
            ball_color[ball] = color
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
                total_count += 1
            ans.append(total_count)    
        return ans
