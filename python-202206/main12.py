# 判斷 bmi 的結果 result ?
# bmi <= 18 過瘦
# 18 < bmi <= 23 正常
# bmi > 23 過胖
# 寫一個計算 bmi 輸入程式,
# 使用者可以輸入身高, 體重
# 若輸入的身高 = 170.5, 體重 = 60, 結果 result 為何 ? (過瘦 or 正常 or 過胖)
# 若輸入的身高 = 180, 體重 = 55, 結果 result 為何 ? (過瘦 or 正常 or 過胖)
# 若輸入的身高 = 160, 體重 = 80.5, 結果 result 為何 ? (過瘦 or 正常 or 過胖)
h = float(input('請輸入身高(cm): '))
w = float(input('請輸入體重(kg): '))
bmi = w / (h/100)**2
print(bmi)
if bmi <= 18:
    print('過輕')
elif bmi > 23:
    print('過重')
else:
    print('正常')


