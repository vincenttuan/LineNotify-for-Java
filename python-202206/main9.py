# 使用者輸入 input
# 透過 int() 可以將 input() 的 str(字串) 資料轉為 int(整數數值) 資料
score = int(input('請輸入分數: '))
print('分數:', score, type(score))

score = score * 1.05  # 分數加 5%
print('分數:', score)
