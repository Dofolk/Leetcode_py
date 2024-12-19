# 這題是給一個 0 ~ n-1 的隨機順序 list，然後連續的子序列如果可以照著順序正常 sort() 的話就是一個區塊，看看給定的 list 最多有幾個區塊
# [1,2,0,3,4] 會有 [1,2,0], [3], [4] 這三個區塊，因為 1,2,0 可以做成 sort()，然後 3 跟 4 可以自己做好就好，順序也是正確的
# 作法有很多種，這邊提供 prefix sum 的作法，因為能夠抵達該位置就要擁有相對應的總和值，所以可以用 prefix sum 來確認當下位置前面的總和有沒有符合
# 認真說，這邊也不用太在意前面是不是真的按照順序來排，因為順序亂掉的話後面一定會要再補回來
# 所以把 prefix sum 當成 check point 就可以知道有幾個 check point，也代表最多可以拆成幾段

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_sum = 0
        sort_sum = 0
        ans = 0
        for i in range(n):
            prefix_sum += arr[i]
            sort_sum += i
            if prefix_sum == sort_sum:
                ans += 1
        return ans
