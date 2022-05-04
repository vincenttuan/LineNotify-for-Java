# LineNotify-for-Java
LineNotify for Java

 * https://notify-bot.line.me/zh_TW/
 * 右上方-登入
 * 右上方-選擇「個人頁面」
 * 發行存取權杖（開發人員用）
 * 放到<a href="https://github.com/vincenttuan/LineNotify-for-Java/blob/main/LineNotify/src/main/java/com/linenotify/Application.java">Application.java</a>中
 * 選定傳送對象與群組(若是用群組必須先把LineNotify加入至群組成員)
 * 最後執行<a href="https://github.com/vincenttuan/LineNotify-for-Java/blob/main/LineNotify/src/main/java/com/linenotify/Application.java">Application.java</a>即可

# LineNotify-for-Python

#基本功能測試
    import requests

    def lineNotifyMessage(token, msg):
        # HTTP 1.1 TLS下去定義的 Token
        # 傳輸層安全性協定（英語：Transport Layer Security，縮寫：TLS）
        # TSL 是更新、更安全的 SSL 版本。
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type" : "application/x-www-form-urlencoded"
        }

        payload = {'message': msg }
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code

    def lineNotifyMessageAndImage(token, msg, picURI):
        # HTTP 1.1 TLS下去定義的 Token
        # 傳輸層安全性協定（英語：Transport Layer Security，縮寫：TLS）
        # TSL 是更新、更安全的 SSL 版本。
        headers = {
            "Authorization": "Bearer " + token  # 不用加入 "Content-Type" : "application/x-www-form-urlencoded"
        }

        payload = {'message': msg }
        files = {'imageFile': open(picURI, 'rb')}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload, files = files)
        return r.status_code

    if __name__ == "__main__":
      token = 'iNlHHliJKPbIjmS2ujkHbTRZiDI8VDc4goD3ZNLDr8G'
      message = 'Girl 女孩'
      #lineNotifyMessage(token, message)
      picURI = "img_1.png"  #圖片位置
      lineNotifyMessageAndImage(token, message, picURI)

  
# LineNotify-for-Arduino D1mini

額外開發版網址: https://arduino.esp8266.com/stable/package_esp8266com_index.json <br />
開發版選擇: LOLIN(WEMOS)D1 mini(clone) <br />
取得Line Notify函式庫，可至Arduino IDE的程式庫管理員打上Line Notify安裝。<br />

    #include <ESP8266WiFi.h>
    #include <TridentTD_LineNotify.h>

    void setup() {
        Serial.begin(9600);
        WiFi.begin("SSID","SSPWD");
        while(WiFi.status() != WL_CONNECTED) {
            delay(500);
            Serial.print(".");
        }
        Serial.println(WiFi.localIP());
    }

    void loop() {
        // 顯示 Line版本
        Serial.println(LINE.getVersion());
        LINE.setToken("存取權杖");
        // 先換行再顯示
        String tempe="溫度:"+String(24)+"℃";   
        String humid="濕度:"+String(55)+"％";
        LINE.notify("\n" + tempe + " ；" + humid);
        delay(50000);
    }
  
