import requests
# LineNotify 通知
# https://notify-bot.line.me/zh_TW/
token = ""
url = "https://notify-api.line.me/api/notify"
msg = input('請輸入要發送的文字訊息: ')
pid = int(input('請輸入貼圖 package id: '))
id = int(input('請輸入貼圖 id: '))

headers = {
    "Authorization": "Bearer " + token
}

payload = {
    "message": msg,
    "stickerPackageId": pid,
    "stickerId": id
}

resp = requests.post(url, headers=headers, params=payload)
print(resp)  # 若回應碼 = 200 表示發送成功

