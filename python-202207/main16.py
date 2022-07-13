# 猜數字遊戲
# 系統隨機產生一個 1~10 之間的數值 ans
# 讓使用者去猜, 若使用者猜的數字大於 ans, 則顯示猜大了
#             若使用者猜的數字小於 ans, 則顯示猜小了
import random

# 產生答案
ans = random.randint(1, 10)
# Play game
while True:
    guess = int(input('請在 1~10 猜一數字: '))
    if guess > ans:
        print('猜大了')
        continue  # 提早進行下一次的迴圈運算
    elif guess < ans:
        print('猜小了')
        continue
    else:
        print('答對了')
        break



