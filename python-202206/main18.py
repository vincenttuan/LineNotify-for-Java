# 爬蟲資料分析
import json
import requests
# 網路資源位置
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
# 抓取原始文字資料
txt = requests.get(url).text
# 將文字資料轉為 json 物件
data = json.loads(txt)
print(data)
print('資料筆數:', len(data))
print('第一筆資料:', data[0])
print('第二筆資料:', data[1])
print('第三筆資料:', data[2])
print('最末筆資料:', data[len(data)-1])
print()
# 資料欄位分析
print('第一筆資料的品名:', data[0]['品名'])
print('第一筆資料的不合格原因:', data[0]['不合格原因'])

print('第二筆資料的品名:', data[1]['品名'])
print('第二筆資料的不合格原因:', data[1]['不合格原因'])

print('第三筆資料的品名:', data[2]['品名'])
print('第三筆資料的不合格原因:', data[2]['不合格原因'])

print('最末筆資料的品名:', data[len(data)-1]['品名'])
print('最末筆資料的不合格原因:', data[len(data)-1]['不合格原因'])
