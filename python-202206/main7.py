# 隨機數 random
import random  # 匯入 random 資源套件

print(random.random())  # 0 <= 隨機數 <1
print(random.randint(0, 100))  # 0~100 的隨機數
# 三星彩
# 0~9 之間選出任意三個數字(數字可以重複)
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
print('三星彩電腦選號:', n1, n2, n3)

