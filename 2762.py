# 這題是給一個數字 list，然後對於連續 subarray 內，任意數字皆不能差距超過 2 ，問在這個 list 裡面有多少合規的 subarray
# ex [5,4,2,4] 合規的有 [5], [4], [2], [4], [5,4], [4,2], [2,4], [4,2,4]，共8個
# 想法就是做 sliding window，但是是動態的，讓 for 跑窗格的右邊位置，並且透過條件檢查的方式來調整窗格左邊的位置
# 用兩個 deque 來記錄當下窗格右邊位置以前，其最大及最小的數字位置在哪裡，然後透過比較當下的最大最小值差距，來看看要不要做窗格左邊界的移動，讓不合規的位置被剔除
# 然後確認完都合規之後就可以做答案的加總，subarray 的數量算簡單，直接 右 - 左 + 1 就可以了，這邊的概念就是當下窗格可以提供的數字有幾個
# 若與前次窗格有重疊，則代表說我有部分的數字提供出來是讓你做 high size 的 subarray，像是: size 為 2 的 [1, 2]，就不是只有單純的一個 [2]

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        L = len(nums)
        max_deque = deque() # store the index of the maximum value w.r.t. the right position of the sliding window
        min_deque = deque() # store the index of the minimum value w.r.t. the right position of the sliding window
        
        for right in range(L):
            while min_deque and nums[min_deque[-1]] >= nums[right]: # check the minimum value with the value of the right position of sliding window
                min_deque.pop() # if the value is large than right, pop out the index
            min_deque.append(right) # append right into deque for next step check
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > 2: # check the value differences
                left += 1 # move left position since the difference bigger than 2
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            ans += right - left + 1
        return ans
