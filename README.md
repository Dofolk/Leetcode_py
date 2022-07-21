# 一些遇到的知識
* 要否定一個敘述的時候不能像C那樣直接加 '!'，要用not。
 * 舉例： not(a==1) 就等於C的 !(a==1)
* python是call by assignment的，遇到mutable的變數時，assignment會是pass by reference，反之則是pass by value
 * mutable變數：set, dictionary, list
 * 可以參考https://medium.com/starbugs/python-%E4%B8%80%E6%AC%A1%E6%90%9E%E6%87%82-pass-by-value-pass-by-reference-%E8%88%87-pass-by-sharing-1873a2c6ac46
 * 或是看python_assignment.pdf
