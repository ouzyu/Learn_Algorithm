# 2次元の累積和(1)
# H x W のマス目がある。
# 上からi行目、左からj列目にあるマス(i, j)には、整数Xi,jが書かれている。
# 以下のQ個の質問に答えるプログラムを作成せよ。
# 質問1:左上(A1, B1)右下(C1, D1)の長方形領域に書かれた整数の総和を求めよ。
# 質問Q:左上(AQ, BQ)右下(CQ, DQ)の長方形領域に書かれた整数の総和を求めよ。

# input
H, W = map(int, input().split())
X = [None] * (H)
Z = [ [0] * (W + 1) for i in range(H + 1)]
for i in range(H):
    X[i] = list(map(int, input().split()))

Q = int(input())
A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 横方向に累積和
for i in range(1, H + 1):
    for j in range(1, W + 1):
        Z[i][j] = Z[i][j - 1] + X[i - 1][j - 1]

# 縦方向に累積和
for j in range(1, W + 1):
    for i in range(1, H + 1):
        Z[i][j] = Z[i - 1][j] + Z[i][j]

# 答え
for i in range(Q):
    print(Z[C[i]][D[i]] + Z[A[i] - 1][B[i] - 1] - Z[A[i] - 1][D[i]] - Z[C[i]][B[i] - 1])