# 判斷成績的 level
# 90 <= score <= 100 印出 A
# 80 <= score <  90  印出 B
# 70 <= score <  80  印出 C
# 60 <= score <  70  印出 D
# 0  <= score <  60  印出 E
score = input('請輸入英文成績: ')
score = int(score)
print('英文成績:', score)
# 判斷成績等第
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:  # elif -> else if
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif 0 <= score < 60:
    print("E")
else:
    print('成績範圍輸入錯誤')
