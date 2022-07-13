# 爬蟲資料分析
# 分析市售米抽檢不合格商品-行政院農委會
import json
import requests
# 網路資源位置
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
# 抓取網路資源文字內容
txt = requests.get(url).text
# 將文字資料轉成 json 物件以利接下來的分析
data = json.loads(txt)
#print(data)
keyword = input('請輸入品名關鍵字: ')
for info in data:
    if keyword in info['品名']:
        print(info['品名'], info['不合格原因'])
