# 搭電梯
# 幸福大樓共有1~7層
import time
print('幸福大樓共有 1 ~ 7 層')
print('進電梯')
current_floor = 1  # 目前電梯所在的樓層
target_floor = 0  # 電梯要去的樓層
while True:
    # 使用者按電梯
    try:
        target_floor = int(input('您現在在 %d 樓, 請問要去哪一個樓層(輸入 0 可以出電梯): ' % current_floor))
    except ValueError:
        print('輸入錯誤請重新輸入')
        continue

    if target_floor == 0:
        print('出電梯')
        break
    if target_floor == current_floor:
        continue
    if target_floor < 1 or target_floor > 7:
        print('樓層請輸入 1 ~ 7 之間')
        continue
    # 進行電梯上下樓的運行
    if target_floor > current_floor:
        print('電梯上樓')
        while target_floor > current_floor:
            print(current_floor)
            current_floor = current_floor + 1
            time.sleep(1)
        print(current_floor)
        print('電梯到了!')
    else:
        print('電梯下樓')
        while target_floor < current_floor:
            print(current_floor)
            current_floor = current_floor - 1
            time.sleep(1)
        print(current_floor)
        print('電梯到了')