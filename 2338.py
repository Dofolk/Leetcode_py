# === Description ===
# 這題是給一個長度 n 及最大值 maxValue，在長度為 n 的 list，問有多少個 ideal array
# ideal array 就是每個元素都是 <= maxValue，而且 arr[i - 1] 可以整除 arr[i]，i.e. arr[i] % arr[i - 1] == 0
#
# === Thought ===
# 這題的出發點就是從質因數分解出發去想，質因數分解可以知道該數字有多少因數可以放進 list 裡面
# 知道質因數之後，可以從質因數的數量去做 H function 的重複組合，n 個位置中要放 p 個質因數
# 這邊要注意的是因為質因數互質，所以可以互相去疊加選取，所以就變成前一個質因數的 H 選完之後直接乘後一個質因數的 H 選取
# 就會變成說，這個質因數我可以選 0~p_i 個，後面的質因數可以選 p_j 個去做組合(相乘)
#
# === Code ===
MOD = 10 ** 9 + 7
max_n = 10 ** 4 + 1
max_prime = 14 # 質因數最多14個，限制條件為 10^4，假設全部質因數都是最小的2也就14個，所以可以設成14就好

sieve = [0] * max_n #紀錄每個數字最小的質因數，用埃拉托斯特尼篩法 (Sieve of Eratosthenes)來處理
for idx in range(2, max_n):
    if sieve[idx] == 0:
        for multi in range(idx, max_n, idx):
            sieve[multi] = idx

prime_count = [[] for _ in range(max_n)] # 紀錄每個數字的各個質因數有幾個，subarray裡面的順序依次表示該數字從小到大的質因數數量有幾個(這邊質因數不一定從2開始，像是57=[1,1]的話就是指1個3跟1個19)

for idx in range(2, max_n): # H function 的 2d array 計算法
    val = idx
    while val > 1:
        p = sieve[val]
        count = 0
        while val % p == 0:
            val //= p
            count += 1
        prime_count[idx].append(count)

combination = [[0] * (max_prime + 1) for _ in range(max_n + max_prime)]
combination[0][0] = 1
for i in range(1, max_n + max_prime):
    combination[i][0] = 1
    for j in range(1, min(i, max_prime) + 1):
        combination[i][j] = (combination[i - 1][j] + combination[i - 1][j - 1]) % MOD

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        for val in range(1, maxValue + 1):
            multi = 1
            for p in prime_count[val]:
                multi = multi * combination[n + p - 1][p] % MOD # 不同質因數的累乘計算
            ans = (ans + multi) % MOD
        return ans
