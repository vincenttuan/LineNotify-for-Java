# 爬蟲資料分析
import json
import requests
# 網路資源位置
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
# 抓取原始文字資料
txt = requests.get(url).text
# 將文字資料轉為 json 物件
data = json.loads(txt)
#print(data)
# 利用 for 迴圈逐筆印出資料
for i in range(len(data)):
    #print(i, data[i])
    # 關鍵字分析 (Ex: 將品名中有'日本'的資料查出)
    if '日本' in data[i]['品名']:
        print(i, data[i]['品名'], data[i]['不合格原因'])
