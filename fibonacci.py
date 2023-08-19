# フィボナッチ数列

# フィボナッチ数列を第N項まで生成する
def fibonacci_list(N):
    fib = [1, 1]
    if N == 1:
        fib = [1]
    else:
        for k in range(2, N):
            fib.append(fib[k - 1] + fib[k - 2])
        return fib

# input
N = int(input())

# output
print(fibonacci_list(N))