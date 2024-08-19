# 這題是給一個整數序列 nums ，然後從中找出連續的子序列(good subarray: Len>2 + conti index)，加總起來是給定植 k 的倍數，能找到就回傳True
# 想法是結合 prefix sum 跟 hash table 來操作，prefix sum的部分來加總目前遇到的值，用 hash table來確認前面是否有互補的值
# 

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2: #長度小於2就不是 good subarray
            return False
        mod_k = {} # hash table用
        prefix = 0
        mod_k[0] = -1 # hash table的餘數為0時，index為-1，因為都沒有東西的時候一定可以整除
        for i, v in enumerate(nums):
            prefix += v #prefix sum
            prefix %= k #prefix sum做餘數(modulo)，因為題目需求，我們只記錄modulo就可以了，不用紀錄到完整的加總數字
            if prefix in mod_k: #確認是否曾經有過一樣的餘數，有一樣的話就可以找到一個區間是可以被6整除的，for ex: 第i,j位的餘數都是5，代表i+1~j這個區間的餘數是0這樣 (1~i)+(i+1~j)的餘數才會也是5
                if i > mod_k[prefix] + 1:#確認長度是否符合要求>2
                    return True
            else:
                mod_k[prefix] = i
        return False
