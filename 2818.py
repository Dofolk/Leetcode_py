# === Description ===
# 從一個正整數陣列 nums 和一個整數 k 開始進行操作，目標是最大化我們的得分。起始分是 1，並且最多可以進行 k 次操作
# 對於操作就是: 選一個未被選過的 subarray nums[L~R](含)，對於裡面的元素找看看誰的質因數最多，就把當前分數乘上最多質因數的這個數字
# 總計操作 k 次之後把結果 modulo 10^9 + 7 後並回傳

# === Thought ===
# 這題的想法就是先把每個數字的質因數數量找出來，可以用 sieve of Eratosthenes 法去算
# 接著就對每個數字的質因數數量最大小的比較，用左邊(left)及右邊(right)兩個 list 來記錄這個數字的質因數數量可以輾壓哪些 subarray 內的所有數字
# 這邊就是用一個 stack 來記錄每個數字之前，誰在 subarray 裡面稱王，把 stack 的數字拿出來比較，看有沒有需要改朝換代，換人當王的
# 接著就可以對把 nums 的 數字，位置，最左邊界及最右邊接給 zip 起來，去 sort 他們，依照數字大小來 sort(因為這樣可以最大化得分)
# 接著就從最大的數字開始看，計算這個數字的位置以及最左有兩邊的統治範圍( (idx-L)*(R-idx) )，來看看這個數字會被乘幾次(選擇subarray的數量)
# 如果比 k 大就只算 k 次，比 k 小就算統治範圍的次數之後從 k 減掉算過的次數，最後回傳就可以了

# === Code Start ===

MOD = 10 ** 9 + 7
Maximum_num = 10 ** 5 + 1
prime_factor_nums = [0] * (Maximum_num)
for num in range(2, Maximum_num):
    if prime_factor_nums[num] == 0:
        for multi in range(num, Maximum_num, num):
            prime_factor_nums[multi] += 1

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stack = []
        for idx, num in enumerate(nums):
            while stack and prime_factor_nums[nums[stack[-1]]] < prime_factor_nums[num]:
                right[stack.pop()] = idx
            if stack:
                left[idx] = stack[-1]
            stack.append(idx)
        
        ans = 1
        for idx, value, L, R in sorted(zip(range(n), nums, left, right), key = lambda x: -x[1]):
            operation_time = (idx - L) * (R - idx)
            if operation_time >= k:
                ans = ans * pow(value, k, MOD) % MOD
                break
            ans = ans * pow(value, operation_time, MOD) % MOD
            k -= operation_time
    
        return ans
