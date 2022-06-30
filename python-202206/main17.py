import requests
# LineNotify 通知
# https://notify-bot.line.me/zh_TW/
token = "FUKeTT7kFNd9myOgiA0theirE4Cxn2R4FSu3ZfDE2T4"
url = "https://notify-api.line.me/api/notify"
msg = input('請輸入要發送的文字訊息: ')

headers = {
    "Authorization": "Bearer " + token
}

payload = {
    "message": msg
}

resp = requests.post(url, headers=headers, params=payload)
print(resp)  # 若回應碼 = 200 表示發送成功

