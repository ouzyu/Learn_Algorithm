# 1次元の累積和(1)
# ある遊園地でN日間にわたるイベントが開催され、i日目にはAi人が来場した。
# 以下のQ個に質問に答えるプログラムを作成せよ。
# 質問1:L1日目からR1日目までの総来場者数は？
# 質問Q:LQ日目からRQ日目までの総来場者数は？

# input
N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [None] * Q
R = [None] * Q


for j in range(Q):
    L[j], R[j] = map(int, input().split())

S = [None] * (N + 1)
S[0] = 0
for i in range(N):
    S[i + 1] = S[i] + A[i]

for j in range(Q):
    print(S[R[j]] - S[L[j] - 1])