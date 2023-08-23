# 動的計画法の復元
# q_4_1で扱ったダンジョンで、今度は最短時間で移動する方法を1つ出力するプログラムを作成せよ。

# input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 動的計画法
dp = [ None ] * (N + 1)
dp[1] = 0
dp[2] = A[0]
for i in range(3, N + 1):
	dp[i] = min(dp[i - 1] + A[i - 2], dp[i - 2] + B[i - 3])

# 答えの復元
# 変数 Place は現在位置（ゴールから進んでいく）
# たとえば入力例の場合、Place は 5 → 4 → 2 → 1 と変化していく
Answer = []
Place = N
while True:
	Answer.append(Place)
	if Place == 1:
		break

	# どこから部屋 Place に向かうのが最適かを求める
	if dp[Place - 1] + A[Place - 2] == dp[Place]:
		Place = Place - 1
	else:
		Place = Place - 2
Answer.reverse()

# output
Answer2 = [str(i) for i in Answer]
print(len(Answer))
print(" ".join(Answer2))