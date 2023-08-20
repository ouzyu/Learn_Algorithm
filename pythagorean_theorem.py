# ピタゴラスの定理(三平方の定理)

# 直角三角形⊿ACBが存在する

import math

# input
AC, BC = map(int, input().split())

AB = (AC ** 2 + BC ** 2)
print(math.sqrt(AB))