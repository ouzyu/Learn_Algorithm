# N個の整数、A₁,A₂,…,An,の中に整数Xが含まれているかどうか

N, X = map(int, input().split())
A = list(map(int, input().split()))
Answer = False

for i in range(N):
    if A[i] == X:
        Answer = True

if Answer == True:
    print("Yes")
else:
    print("No")