# 動的計画法
# あるダンジョンにはN個の部屋があり、1からNまでの番号が付けられている。個のダンジョンは一方通行であり、通路を介して1つ先または2つ先の部屋に移動することが出来る。
# 各通路における移動時間は以下の通りである。
# 部屋i-1から部屋iに向かう通路を通るのにAi分(2 <= i <= N)かかる
# 部屋i-2から部屋iに向かう通路を通るのにBi分(3 <= i <= N)かかる
# 部屋1から部屋Nに移動するのに、最短何分かかるか。

# input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 動的計画法
dp = [ None ] * (N+1)
dp[1] = 0
dp[2] = A[0]
for i in range(3, N+1):
	dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

# output
print(dp[N])