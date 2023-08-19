#  余りの計算(2):累乗　繰り返し二乗法
# aのb乗の値をmで割った余りを求めよ

def Power(a, b, m):
    p = a
    Answer = 1
    for i in range(30):
        wari = 2 ** i
        if (b // wari) % 2 == 1:
            Answer = (Answer * p) % m
        p = (p * p) % m
    return Answer

# input
a, b = map(int, input().split())

# output
print(Power(a, b, 1000000007))