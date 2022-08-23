# 這題就是依照數字高低給名次
# 作法是先建立一個位置的字典，然後再 sort list 拿到順序，依照順序把名次放上去

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        D = dict()
        ans = [""]*len(score)
        for i in range(len(score)):
            D[score[i]] = i
        score.sort(reverse = True)
        idx = 0
        for x in score:
            if idx == 0: ans[D[x]] = "Gold Medal"
            elif idx == 1: ans[D[x]] = "Silver Medal"
            elif idx == 2: ans[D[x]] = "Bronze Medal"
            else: ans[D[x]] = str(idx+1)
            
            idx += 1
        
        return ans
