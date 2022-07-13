import requests
token = '9vT6GKT6E64IVhs3MLzOtRD0O8Yd9LAd7N7R1BVxtBO'
url = "https://notify-api.line.me/api/notify"
# HTTP 標頭資訊, 設定授權 token
# Basic 用在存取一個網站、網域的時候
# Bearer 則是用於存取 Protect Resource 的時候
headers = {
    "Authorization": "Bearer " + token
}
# 設定傳送的訊息內容
msg = input('請輸入文字訊息: ')
# 設定傳送的貼圖
stickerPackageId = 6136
stickerId = 10551377
payload = {
    "message": msg,
    "stickerPackageId": stickerPackageId,
    "stickerId": stickerId
}
# 傳送
resp = requests.post(url, headers=headers, params=payload)
print(resp)  # 若看到 200 表示發送成功
