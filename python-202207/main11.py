# 所輸入的字串是否是都是0~9的數值
score = input('請輸入成績: ')
print(score.isdigit())  # 判斷字串內容是否都是數字
# 判斷
if score.isdigit():
    score = int(score)
    print('成績:', score)
else:
    print('成績資料錯誤')
