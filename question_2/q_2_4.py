# 二次元の累積和(2)
# ALGO王国はH x Wのマス目で表される。最初は、どのマスにも雪が積もっていないが、これからN日間に渡って雪が降り続ける。
# 上からi行目、左からj列目のマスを(i, j)とする時、t日目には
# 「マス(At, Bt)を左上とし、マス(Ct, Dt)を右下とする長方形領域」の積雪が1㎝だけ増加することが予想されている。
# 最終的な各マスの積雪を出力するプログラムを作成せよ。

# input
H, W, N = map(int, input().split())
A = [ None ] * N
B = [ None ] * N
C = [ None ] * N
D = [ None ] * N
X = [ None ] * (W)
for t in range(N):
	A[t], B[t], C[t], D[t] = map(int, input().split())

# 各日について加算
X = [ [ 0 ] * (W + 2) for i in range(H + 2) ]
Z = [ [ 0 ] * (W + 2) for i in range(H + 2) ]
for t in range(N):
    X[A[t]][B[t]]           += 1
    X[A[t]][D[t] + 1]       -= 1
    X[C[t] + 1][B[t]]       -= 1
    X[C[t] + 1][D[t] + 1]   += 1

# 二次元累積和
for i in range(1, H+1):
	for j in range(1, W+1):
		Z[i][j] = Z[i][j-1] + X[i][j]
for j in range(1, W+1):
	for i in range(1, H+1):
		Z[i][j] = Z[i-1][j] + Z[i][j]

# output
for i in range(1, H+1):
	for j in range(1, W+1):
		if j >= 2:
			print(" ", end="")
		print(Z[i][j], end="")
	print("")