# 余りの計算(1)
# 黒板に0という整数が書かれている。黒板に書かれた整数に対してN回の操作を行う。
# i回目の操作は文字Tiと整数Aiで表され、その内容は以下となる。
# Ti =+ の時:Aiを足す。
# Ti =- の時:Aiを引く。
# Ti =* の時:Aiを掛ける。
# 各操作が終わった後について、黒板に書かれた整数を10000で割った余りを出力するプログラムを作成せよ。

# input
N = int(input())
T = [None] * N
A = [None] * N
for i in range(N):
    T[i], A[i] = input().split()
    A[i] = int(A[i])

# output
Answer = 0
for i in range(N):
    if T[i] == '+':
        Answer += A[i]
    if T[i] == '-':
        Answer -= A[i]
    if T[i] == '*':
        Answer *= A[i]
    if Answer < 0:
        Answer += 10000

    Answer %= 10000
    print(Answer)