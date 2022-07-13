# 綜合練習
# 寫一個 計算 BMI 輸入程式
# 使用者可以輸入身高, 體重
# 並且系統可以判斷 bmi 值的結果是正常, 過胖還是過瘦
#  <=18  >18 ~ 23  >23
#  過瘦     正常    過胖
h = input('請輸入身高: ')
w = input('請輸入體重: ')
if h.isdigit() and w.isdigit():  # 檢查所輸入的是否都是數值
    h = int(h)
    w = int(w)
    bmi = w / (h/100)**2
    print(bmi)
    if bmi <= 18:
        print('過瘦')
    elif bmi > 23:
        print('過胖')
    else:
        print('正常')
else:
    print('輸入資料錯誤')
