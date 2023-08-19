# 最大公約数:Greatest Common Divisor
# 整数AとBの最大公約数を求めるプログラムを作成せよ。

def GCD(A, B):
	while A >= 1 and B >= 1:
		if A >= B: # 大きい方の数字を判定
			A = A % B
		else:
			B = B % A
	if A >= 1:
		return A
	return B

# input
A, B = map(int, input().split())
print(GCD(A, B))