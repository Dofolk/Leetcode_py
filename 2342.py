class Solution:
      def maximumSum(self, nums: List[int]) > int:
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
                        if max_two[value][1] != 1:
                                          s = max_two[value][0] + max_two[value][1]
                                          if s > M:
                                                                M = s
                                                    return M
