# 這題是給兩串版本的編號(version : X.XX.XXX)，然後去比較看看哪邊比較晚發行的
# 做法就是先做 split 把數字都切開來，然後把兩個版本編號都變成一樣長的 list
# 最後再逐個變成數字比較就可以知道誰比較早比較晚了

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        l1, l2 = len(v1), len(v2)
        if l1 < l2:
            for i in range(l2-l1): v1.append('0')
        elif l2 < l1:
            for i in range(l1-l2): v2.append('0')
        for i in range(max(l1,l2)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0
