# 配列の二分探索
# 小さい順に並べられている、要素数Nの配列A = [A1, A2,…, AN]がある。
# 要素Xは配列Aの何番目に存在するかを出力せよ。

def search(x, A):
    L = 0
    R = N - 1
    while L <= R:
        M = (L + R) // 2
        if x < A[M]:
            R = M - 1
        if x == A[M]:
            return M
        if x > A[M]:
            L = M + 1
    return -1

# input
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索を行う
Answer = search(X, A)
print(Answer + 1)