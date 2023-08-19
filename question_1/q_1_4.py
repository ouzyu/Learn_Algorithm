# 整数Nが10進法表記で与えられる。Nを2進法に変換した値を出力する。

# input 
N = int(input())

# 2進法に変換
for x in [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
    wari = (2 ** x)
    print((N // wari) % 2, end = '')
