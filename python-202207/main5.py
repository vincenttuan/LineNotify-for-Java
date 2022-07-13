# 變數應用 III
# 已知半徑 r ,
# 求圓面積 pi * r**2
# 求球體積 4/3 * pi r**3
import math  # 載入數學資源
r = 10
pi = math.pi
print('pi:', pi)
area = pi * r**2
print('半徑:', r, '圓面積:', area)
volume = 4/3 * pi * r**3
print('半徑:', r, '球體積:', volume)
