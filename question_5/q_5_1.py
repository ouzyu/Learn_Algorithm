# 素数判定
# 以下のQ個の質問に応えるプログラムを作成せよ
# 質問1:整数X1は素数か
# 質問Q:整数XQは素数か

def isPrime(N):
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT + 1):
        if N % i == 0:
            return False
    return True

# input
Q = int(input())
X = [None] * Q
for i in range(Q):
    X[i] = int(input())

# output
for i in range(Q):
    Answer = isPrime(X[i])
    if Answer == True:
        print("Yes")
    else:
        print("No")