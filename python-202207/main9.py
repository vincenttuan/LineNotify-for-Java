# 程式判斷與輸入
# if - elif - else
# input() -> 使用者輸入 python 會得到字串(str)
#            若有必要要進行適當的轉型
# type() 就是顯示資料型態
score = input('請輸入分數: ')
print(score, type(score))

score = int(score)  # 進行適當的轉型, int() 轉型整數
print(score, type(score))

# 判斷是否及格 ?
if score >= 60:
    print('及格')
else:
    print('不及格')
