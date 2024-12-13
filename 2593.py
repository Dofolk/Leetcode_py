# 這題是給一個數字 list，然後取最小值後將其兩旁的位置做標記，被座標季之後不可取用，取得最小值後與之前獲得的最小值們做加總，問最後加總會是多少
# 想法是 divide and conquer，用 deque 來記錄遞減的區間的數字們，遇到遞增的轉折時開始對前面遞減的區段做跳位加總(因為要兩旁位置做標記不能取用)
# 因為遞減轉遞增的轉折點，取全域最小數字的時候就會取到這個轉折點，因為他的兩旁都是比較大的，所以就可以做一個 divide conquer 做數字加總
# ex 4,3,2,5 -> 取 2 標記 3, 5
# 另一種想法就是，反正要取最小值，一定先把 local minimum 先拿了就對了，畢竟都是 local minimum 了，其左右兩邊的較大數值一定是會先被 mark 掉的
# 因為間隔兩個位職以上就不會影響到 local minimum 了，所以給它取用就對了


class Solution:
    def findScore(self, nums: List[int]) -> int:
        value = 0
        L = len(nums)
        q = deque()

        for idx in range(L):
            if q and nums[idx] >= q[-1]:
                skip = False
                while q:
                    add = q.pop()
                    if not skip:
                        value += add
                    skip = not skip
                continue
            q.append(nums[idx])
        
        skip = False
        while q:
            add = q.pop()
            if not skip:
                value += add
            skip = not skip
        return value
