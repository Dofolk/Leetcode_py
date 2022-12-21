# 這題是要做一個 Trie 的搜尋，只是搜尋的時候會有 . 出現，代表任意字母
# 做法跟208類似，先用 dict 做 Trie 出來，然後順存新增的字母長度(用來加速判斷的)
# 然後就用 DFS，遇到 . 就直接往下找所有的 sub 會不會對

class WordDictionary:

    def __init__(self):
        self.root = {}
        self.leng = set()

    def addWord(self, word: str) -> None:
        self.leng.add(len(word))
        d = self.root
        for s in word:
            d = d.setdefault(s,{})
        d[None] = None

    def search(self, word: str) -> bool:
        def find(word, node):
            if not word: return None in node
            char, word = word[0], word[1:]
            if char != '.':
                return char in node and find(word, node[char])
            return any(find(word, kid) for kid in node.values() if kid)
        return find(word, self.root) if len(word) in self.leng else False

                



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
