# 赤・青・白の3枚のカードがある。それぞれのカードに1以上N以下の整数を書かなければならない。
# 3枚のカードの合計をKにするような書き方は何通りあるか。

# input
N, K = map(int, input().split())
Answer = 0

# 全探索
for x in range(1, N + 1):
    for y in range(1, N + 1):
        z = K - x - y
        if z >= 1 and z <= N:
            Answer += 1

# output
print(Answer)