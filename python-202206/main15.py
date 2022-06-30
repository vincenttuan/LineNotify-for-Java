# 猜數字與電腦對戰
# 1~99 猜一個數字
import random
import time
min = 1
max = 99
ans = random.randint(min, max)
while True:
    # 使用者猜
    guess = int(input('使用者請在 %d ~ %d 猜一數字: ' % (min, max)))
    # 驗證合法性
    if guess < min or guess > max:
        print('數字超過合法範圍, 請重新輸入!')
        continue

    if guess < ans:
        min = guess
    elif guess > ans:
        max = guess
    else:
        print('恭喜使用者猜對了')
        break
    # 電腦猜
    print('電腦計算中...')
    time.sleep(1)  # 停一秒鐘
    pc_guess = random.randint(min, max)  # 模擬電腦猜數字
    print('電腦在 %d ~ %d 猜一數字: %d' % (min, max, pc_guess))
    if pc_guess < ans:
        min = pc_guess
    elif pc_guess > ans:
        max = pc_guess
    else:
        print('恭喜電腦猜對了')
        break
