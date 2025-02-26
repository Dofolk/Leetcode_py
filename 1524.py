# 這題是給一個正整數 list，然後去看看所有總和是奇數的 subarray 有幾個
# 這裡可以知道說，奇數只能透過一奇一偶相加獲得，所以這邊就可以變成去考慮有多首個基數偶數可以去做配對
# 因為要找所有的 subarray，這部分可以透過 prefix 的做法來找比較有效率
# 這邊可以用 prefix 來看看每個位置的 prefix sum 是奇數還是偶數，透過 prefix 的結果可以往前去推算奇偶 pair 有幾對
# prefix 可以成功的原因就是，對於奇偶配對就可以看成是一個符合條件的 subarray， prefix_i - prefix_j = sum(a_i + ... + a_j)
# 這樣我可以只考慮奇偶數量來找何目標的 subarray 
# 所以就變成去計算 prefix 有多少奇數跟偶數，然後做相乘就可以找出總共有幾個 subarray 了
# 這邊要注意的是偶數計算起始是 1，因為 0 在這邊也要算進來

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_count, even_count, prefix = 0, 1, 0
        for val in arr:
            prefix += val
            if prefix % 2:
                odd_count += 1
            else:
                even_count += 1
        return (odd_count * even_count) % (10**9 + 7)
