class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        
# 直接做，把 nums1後面的0直接先替換成nums2的，最後再sort
# 另一個作法就是用three pointer
# 從 nums1的尾端開始跑，最大的放後面，然後慢慢的依序往前擺放

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        id1 = m - 1
        id2 = n - 1
        for p in range(m + n - 1, -1, -1):
            if id2 < 0:
                break
            if id1 >= 0 and nums1[id1] > nums2[id2]:
                nums1[p] = nums1[id1]
                id1 -= 1
            else:
                nums1[p] = nums2[id2]
                id2 -= 1
