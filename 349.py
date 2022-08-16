# 這題是要找出兩個 list 有哪些元素是重疊的
# 第一個做法就是一個一個直接找直接算
# 第二個方法就是用 & 來找，單行解法

class Solution:

# Solution 1
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = []
        l1 = len(nums1)
        l2 = len(nums2)
        for i in nums1:
            if i in nums2 and i not in ls:
                ls.append(i)
        return ls
      
# Solution 2
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list( set(nums1) & set(nums2) )
