# 這題是做 two sum，只是給的是非遞減序列
# 做法就是用一個字典來存走過的插植跟位置，走到後面發現有符合的插值就直接回傳就可以了

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            if numbers[i] not in dic:
                dic[target - numbers[i]] = i
            else:
                return [dic[numbers[i]] + 1, i + 1]
