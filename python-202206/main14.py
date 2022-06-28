# 猜數字遊戲
# 系統隨機產生一個 1~10 之間的數值 ans
# 使用者來猜 guess, 若使用者猜的數字大於 ans, 則顯示猜大了
#                  若使用者猜的數字小於 ans, 則顯示猜小了
#                  若使用者猜的數字等於 ans, 則顯示 bingo, 跳離迴圈
import random

# 產生答案
ans = random.randint(1, 10)
# Play game
while True:
    guess = int(input('請在 1~10 猜一個數字:'))
    if guess > ans:
        print('猜大了')
        continue  # 提早執行下一次的迴圈
    elif guess < ans:
        print('猜小了')
        continue  # 提早執行下一次的迴圈
    else:
        print('Bingo')
        print('ans:', ans)
        break  # 跳離迴圈
