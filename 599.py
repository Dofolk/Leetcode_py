# 這題是給兩個字串 list，然後找出重疊的文字，依照該字分別在 list 的 index 相加，找出最小的值是哪些字
# 做法就是把其中一個 list 當 hashmap，然後再從剩下的 list 逐字搜尋，比較數字大小，儲存文字

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = float('inf')
        stack = []
        for i in range(len(list2)):
            if list2[i] in list1:
                s = i + list1.index(list2[i])
                if s<m:
                    stack.clear()
                    stack.append(list2[i])
                    m = s
                elif s == m:
                    stack.append(list2[i])
        
        return stack
                    
                    
