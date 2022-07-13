# 迴圈
# 重複執行任務
# break 跳出迴圈
# continue 提早進行下一次的迴圈
import random

# 任務: 印出 1~100 隨機數
# 限制: 若印出 77 則 break 停止迴圈運行
while True:
    x = random.randint(1, 100)
    print(x)
    if x == 77:
        break
