# 答えで二分探索
# N台のプリンターがあり、1からNまでの番号が付けられている。プリンターiはAi秒ごとにチラシを1枚印刷する。
# すなわち、スイッチを入れてからAi秒後、2Ai秒後、3Ai秒後,…に印刷する。
# すべてのプリンターのスイッチを同時に入れた時、K枚目のチラシが印刷されるのは何秒後か。

# 答えが x 以下かを判定し、Yes であれば true、No であれば false を返す関数
def check(x, N, K, A):
	sum = 0
	for i in range(N):
		sum += x // A[i] # 「x÷A[i]」の小数点以下切り捨て

	if sum >= K:
		return True
	return False

# input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索
# Left は探索範囲の左端を、Right は探索範囲の右端を表す
Left = 1
Right = 10 ** 9
while Left < Right:
	Mid = (Left + Right) // 2
	Answer = check(Mid, N, K, A)

	if Answer == False:
		Left = Mid + 1 # 答えが Mid+1 以上であることが分かる
	if Answer == True:
		Right = Mid # 答えが Mid 以下であることが分かる

# output（このとき Left=Right になっている）
print(Left)