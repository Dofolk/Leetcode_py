# 這題是要找出那些元素是重複的，所以出現好寄次的元素就會在答案的 list 裡面出現好幾次
# 做法就是找看看有沒有重複，有的話就家到達按理並且從原本的 list 移除掉

class Solution:

# Solution 1
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = []
        L1 = len(nums1)
        L2 = len(nums2)
        if L1>=L2:
            for i in nums2:
                if i in nums1:
                    ls.append(i)
                    nums1.remove(i)
        else:
            for i in nums1:
                if i in nums2:
                    ls.append(i)
                    nums2.remove(i)
                    
        return ls
       
# Solution 2
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = []
        for i in nums1:
            if i in nums2:
                ls.append(i)
                nums2.remove(i)
        return ls
