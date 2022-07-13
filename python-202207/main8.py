# 計算二點間的距離
# A(x1, y1)  B(x2, y2)
# 設 A(10, 20)  B(55, 120)
# 求 AB 二點間的距離 ?
import math
# 開根號
print(math.sqrt(9))  # 3
# 指數
print(3**2)
print(math.pow(3, 2))  # 3**2
x1, y1 = 10, 20   # A 點
x2, y2 = 55, 120  # B 點
dx = math.pow(x1-x2, 2)
dy = math.pow(y1-y2, 2)
d = math.sqrt(dx + dy)
print('距離:', d)
