# トリボナッチ数列

# 1, 1, 2から始まるN項のトリボナッチ数列を生成
def tribonacci_list(N, t0, t1, t2):
    tri = [t0, t1, t2]
    if N == 1:
        tri = [t0]
    elif N == 2:
        tri = [t0, t1]
    else:
        for k in range(3, N):
            tri.append(tri[k - 1] + tri[k - 2] + tri[k - 3])
    return tri

# input
N, t0, t1, t2 = map(int, input().split())

# output
print(tribonacci_list(N, t0, t1, t2))