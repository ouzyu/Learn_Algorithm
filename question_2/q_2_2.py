# 1次元の累積和(2)
# ある会社ではD日間にわたってイベントが開催され、N人が出席する。
# 参加者i(i = 1,2,…,N)はLi日目からRi日目まで出席する予定である。
# 各日の出席数を出力するプログラムを作成せよ。

# input
D = int(input())
N = int(input())
L = [None] * N
R = [None] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

# 前日比に加算
B = [0] * (D + 2)
for i in range(N):
    B[L[i]] += 1
    B[R[i] + 1] -= 1

# 累積和を取る
Answer = [None] * (D + 2)
Answer[0] = 0
for d in range(1, D + 1):
    Answer[d] = Answer[d - 1] + B[d]

# output
for d in range(1, D + 1):
    print(Answer[d])