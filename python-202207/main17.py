# 猜數字與電腦對戰版
# 1~99 猜一數字
import random
import time
min_value, max_value = 1, 99
ans = random.randint(min_value, max_value)
# Play
while True:
    # 使用者猜
    user_guess = input('使用者請在 %d~%d 猜一數字: ' % (min_value, max_value))
    user_guess = int(user_guess)
    # 驗證合法性
    if user_guess < min_value or user_guess > max_value:
        print('數字範圍錯誤, 請重新輸入')
        continue
    # 判斷 user 是否猜中
    if user_guess < ans:
        min_value = user_guess
    elif user_guess > ans:
        max_value = user_guess
    else:
        print('使用者猜對! Win')
        break
    # ----------------------------------------------------
    # 電腦猜
    print('電腦計算中...')
    time.sleep(1)  # 停一秒 (模擬電腦運算)
    pc_guess = random.randint(min_value, max_value)
    print('電腦在 %d ~ %d 猜一數字: %d' % (min_value, max_value, pc_guess))
    # 判斷 pc 是否猜中
    if pc_guess < ans:
        min_value = pc_guess
    elif pc_guess > ans:
        max_value = pc_guess
    else:
        print('電腦猜對了! Win')
        break

