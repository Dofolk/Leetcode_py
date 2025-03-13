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
# 好用技巧
* 差分陣列(Difference Array)
  * 差分陣列可以用在累積量的處理，像是給一堆區間以及區間內每個位置要增加的數值，這樣就可以使用差分陣列的想法搭配上前綴和，來找出每個位置的累積量是多少
    差分陣列理解的方式也很簡單，所以可以想成是在位置 a_start 的時候紀錄一個正數代表說從這邊開始有區間要加數字
    然後在對應的區間結尾 a_end 紀錄一個等值的負數，代表說這個區間到這邊結束，要把加進來的數值給消去
    因為會搭配 prefix 來記錄累積量，所以區間開頭 a_start 的時候加上的數值會一直保留著，直到遇到 a_end 的負數相抵銷掉時才結束累積
    這時候就完成了一個區間的累積量計算，當多個區間湊再一起的時候就可以知道每個位置再給定的區間累積計算下能達到多大的數字
  * 反過來想也不會很困難，假設我知道某個 prefix 的結果也可以做出差分陣列，差分陣列的最一開始就是 prefix 的頭，代表說這個一開始要有多少數字
    接下來就把後面的數字減去前面的數字，代表說要從前一個數字變成後一個數字需要多少東西加進來或是扣掉
    也就是說我要往後走到一樣的成果時，當下位置需要多少的累積量加入才可以達成
  * EX least_prefix = [2,0,2,xxxx]，區間計算是[left,right,add_value] = [0,2,1], [0,2,1], [1,2,1]
    這邊可以看得出來第一個區間說從 idx 0 的時候要加 1，所以 diff_arr = [1,0,0,-1]，這個 diff_arr 在 prefix 的操作下就是 [1,1,1,0] 也就是我們需要的區間內每個位置都加 1
* TBD
