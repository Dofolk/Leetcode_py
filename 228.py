class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ls = []
        p1, p2 = 0, 0
        for i in range(len(nums)):
            if i+1<=len(nums)-1:
                if (nums[i]+1)==nums[i+1]:
                    p2 += 1
                elif p1 != p2:
                    ls.append(str(nums[p1]) + '->' + str(nums[p2]))
                    p1 = p2 + 1
                    p2 += 1
                elif p1 == p2:
                    ls.append(str(nums[p1]))
                    p1 += 1
                    p2 += 1
            else:
                if p1 != p2:
                    ls.append(str(nums[p1]) + '->' + str(nums[p2]))
                else:
                    ls.append(str(nums[p1]))
                
        return ls
      
# 這題要在給定的 list 裡面找連續的區間，並且存成字串的形式 a->b
# 做法就是一個一個找，用到 two pointer 來做定位
# 要注意的點是在更新 pointer 位置的時候記得 +1 讓兩個 pointer 都可以往後跑到下一個區間去
