# 這題給了兩個 list ，一個是要找的數字，一個是給好的數字順序，從數字順序找看看該數字後面有沒有更大的數字，有就存數字，沒有就存-1
# 做法就是需要一個控制點，來看看有沒有找到數字，反正遇到大的數字就存起來，沒有的話就繼續找，找到最後flag還事證的話就說明沒有更大的了，存-1

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        flag = True
        
        for i in nums1:
            idx = nums2.index(i)
            flag = True
            for n in range(idx,len(nums2)):
                if nums2[n] > i:
                    ans.append(nums2[n])
                    flag = False
                    break
            if flag:
                ans.append(-1)
        
        return ans
