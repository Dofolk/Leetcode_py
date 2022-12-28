# 這題是要找 list 裡面出現次數大於 總長度/3 的數字有哪些
# 做法就是直接 call counter，然後找看看哪些是大於的就回傳就好

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict={}
        for i in nums:
            if i in my_dict:
                my_dict[i]+=1
            elif len(my_dict)<2:
                my_dict[i]=1
            else:
                temp={}
                for c in my_dict:
                    my_dict[c]-=1
                    if my_dict[c]>=1:
                        temp[c]=my_dict[c]
                my_dict=temp
        ans = [k for k in my_dict if nums.count(k) > len(nums) // 3]          

        return ans
      
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        L = len(nums)//3
        C = collections.Counter(nums)
        ls = list()
        
        for v in C:
            if C[v] > L:
                ls.append(v)
        return ls
