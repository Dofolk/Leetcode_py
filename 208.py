# 這題是要做出 Trie(音 Try)
# 做法就是宣告成字典，然後一直疊下去
# 找的時候就是一層一層找有沒有存在，找到最後一層的時候看看有沒有結束符號(#)，有就沒問題，沒有就代表沒這個字
# Startwith 就是直接一層層找就可了

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        D = self.root
        for s in word:
            if s not in D:
                D[s] = {}
            D = D[s]
        
        D['#'] = '#'

    def search(self, word: str) -> bool:
        d=self.root.copy()

        for c in word:
            if c in d:
                d=d[c]
            else:
                return False

        if '#' in d:
            return True
    
        return False

    def startsWith(self, prefix: str) -> bool:
        d=self.root.copy()

        for c in prefix:
            if c in d:
                d=d[c]                
            else:
                return False
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
