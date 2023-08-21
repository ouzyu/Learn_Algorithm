# 半分全列挙
# A・B・C・Dの4つの箱がある。各箱には、以下のN枚のカードが入っている。
# 箱Aには整数A1,A2,…,ANが書かれたカードがある。
# 箱Bには整数B1,B2,…,BNが書かれたカードがある。
# 箱Cには整数C1,C2,…,CNが書かれたカードがある。
# 箱Dには整数D1,D2,…,DNが書かれたカードがある。
# それぞれの箱から1枚ずつカードを取り出し、取り出した4枚のカードに書かれた整数の合計がKとなる可能性はあるか、判定せよ

import bisect
import sys

# input
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# 配列 P を作成
P = []
for x in range(N):
	for y in range(N):
		P.append(A[x] + B[y])

# 配列 Q を作成
Q = []
for z in range(N):
	for w in range(N):
		Q.append(C[z] + D[w])

# 配列 Q を小さい順にソート
Q.sort()

# 二分探索
for i in range(len(P)):
	pos1 = bisect.bisect_left(Q, K - P[i])
	if pos1 < N * N and Q[pos1] == K - P[i]:
		print("Yes")
		sys.exit(0)

# 見つからなかった場合
print("No")