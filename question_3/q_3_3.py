# しゃくとり法
# N個の整数が黒板に書かれている。書かれている整数は小さい順にA1,A2,…,Anとなる。
# 異なる2つの整数のペアを選ぶ方法は全部でN(N-1)/2通りあるが、その中で差がK以下である選び方は何通りあるか。

# input（A は 0 番目から始まることに注意）
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 配列の準備（R は 0 番目から始まることに注意）
R = [ None ] * N

# しゃくとり法
for i in range(0, N - 1):
	# スタート地点を決める
	if i == 0:
		R[i] = 0
	else:
		R[i] = R[i - 1]

	# ギリギリまで増やしていく
	while R[i] < N - 1 and A[R[i] + 1] - A[i] <= K:
		R[i] += 1

# output
Answer = 0
for i in range(0, N-1):
	Answer += (R[i] - i)
print(Answer)