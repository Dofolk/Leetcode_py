# 檔案們
* 參考資料裡面放一些之前有用到的資料來源
* Extra裡面放的是遇到非Leet的問題
* 一般Leet問題就直接放在外面這邊，ctrl+F很好用

# 一些遇到的知識
* 要否定一個敘述的時候不能像C那樣直接加 '!'，要用not。
  * 舉例： not(a==1) 就等於C的 !(a==1)
* python是call by assignment的，遇到mutable的變數時，assignment會是pass by reference，反之則是pass by value
  * mutable變數：set, dictionary, list
  * 可以參考https://medium.com/starbugs/python-%E4%B8%80%E6%AC%A1%E6%90%9E%E6%87%82-pass-by-value-pass-by-reference-%E8%88%87-pass-by-sharing-1873a2c6ac46
  * 或是看參考資料/python_assignment.pdf
* 在定義class的時候， \_\_init\_\_ 裡面寫的東西就是一個最這個class的初始化(記得都要self.xxx)，可以在class裡面通用，所有操作都可以對它做，也可以知道說現在這個class裡面有包含哪些東西
  * 像是 link list的話，這裡面就會有兩個值 self.val 跟 self.next ，代表說一個是存值一個是下一個點是誰
  * 或是假設要建立出 list 的話，這裡就直接 self.ls = [] ，這樣就可以建立一個名為 ls 的 list在這個 class 裡面來用
* 在做數字操作的時候可以不用太擔心數值的上限，像是 2^31 2^32等等的，python 都可以去吃數值，不像 C/C++ 每個宣告的變數都有其數值的上限
* 459題，KMP算法就是把兩個字串做比對，看看能比對多長，有一樣就繼續加1，沒有的話就用 while 來降低
  * 參考 https://www.evanlin.com/about-kmp/
  * https://zh.wikipedia.org/zh-tw/KMP%E7%AE%97%E6%B3%95
* 208題，Trie是用字母做成tree形式的搜尋法(想法就是一層一層疊起來就對了)
  * 參考 https://zh.wikipedia.org/zh-tw/Trie
  * https://ithelp.ithome.com.tw/articles/10248152
