# 隨機數 random 0 <= x < 1
import random  # 載入 random 資源套件

print(random.random())  # 產出隨機數
print(random.randint(0, 100))  # 產出 0~100 的隨機數

# 電腦選號四星彩
# 0~9 之間選出任意四個數字(可以重複)
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
print('四星採電腦選號:', n1, n2, n3, n4)


