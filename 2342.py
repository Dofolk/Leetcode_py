# 這題是給一格數字 list nums，然後找任意兩個相異位置的數字，如果兩個數字的各個位數數字總和一樣的話，就把兩個數字相加
# 問 list 裡面最大的總和數字是多少
# 想法就是用一個字典來記錄位數數字總和以及對應的兩個最大的數字，當遇到一個新數字進來就先去確認字典的存在性
# 確認完存在之後就去看看新進來的數字會不會去替換掉最大或第二大的數字，這邊就依據條件操作一下數字的更替
# 最後就是依據字典逐個確認最大的數字總和是多少，再回傳就可以了

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_two = dict()
        M = -1
        for num in nums:
            digit_sum, digit_num = 0, num
            while digit_num:
                digit_sum += digit_num%10
                digit_num //= 10
            if digit_sum in max_two:
                if num >= max_two[digit_sum][0]:
                    max_two[digit_sum][0], max_two[digit_sum][1] = num, max_two[digit_sum][0]
                elif num > max_two[digit_sum][1]:
                    max_two[digit_sum][1] = num
            else:
                max_two[digit_sum] = [num, -1]
        for value in max_two:
            if max_two[value][1] != -1:
                s = max_two[value][0] + max_two[value][1]
                if s > M:
                    M = s
        return M
