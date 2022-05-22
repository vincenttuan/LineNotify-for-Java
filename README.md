# LineNotify-for-Java
LineNotify API 文件
 * https://notify-bot.line.me/doc/en/ (API文件)
 * https://developers.line.biz/en/docs/messaging-api/sticker-list/ (sticker 小圖)

LineNotify for Java
 * https://notify-bot.line.me/zh_TW/ (主網頁) 
 * 右上方-登入
 * 右上方-選擇「個人頁面」
 * 發行存取權杖（開發人員用）
 * 放到<a href="https://github.com/vincenttuan/LineNotify-for-Java/blob/main/LineNotify/src/main/java/com/linenotify/Application.java">Application.java</a>中
 * 選定傳送對象與群組(若是用群組必須先把LineNotify加入至群組成員)
 * 最後執行<a href="https://github.com/vincenttuan/LineNotify-for-Java/blob/main/LineNotify/src/main/java/com/linenotify/Application.java">Application.java</a>即可

# LineNotify-for-Java(簡單版)

    import java.io.DataOutputStream;
    import java.net.HttpURLConnection;
    import java.net.URL;

    public class LineNotifyDemo {

        public static void main(String[] args) throws Exception {
            // 1. 要發送的資料
            String message = "Hello Java 中文";
            // 2. 存取權杖(也稱為:授權 Token)
            String token = "存取權杖";
            // 3. Line Notify 的發送位置
            String lineNotifyUrl = "https://notify-api.line.me/api/notify";
            // 4. 發送前設定 -------------------------------------------------------------------------
            // 發送文字
            byte[] postData = ("message=" + message).getBytes("UTF-8");
            // 發送文字 + 縮略圖 + 網路圖片
            // String picurl = "https://image.cache.u-car.com.tw/articleimage_1091049.jpg";
            // byte[] postData = ("message=" + message + "&stickerPackageId=1&stickerId=113&imageThumbnail=" + picurl + "&imageFullsize=" + picurl).getBytes("UTF-8");

            int postDataLength = postData.length;
            URL url = new URL(lineNotifyUrl);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Authorization", "Bearer " + token); // 一定要加
            conn.setRequestProperty("charset", "utf-8"); // 可以不用加
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded"); // 可以不用加
            conn.setRequestProperty("Content-Length", Integer.toString(postDataLength)); // 可以不用加
            conn.setUseCaches(false);
            // 5. 訊息發送 ---------------------------------------------------------------------------
            try (DataOutputStream wr = new DataOutputStream(conn.getOutputStream())) {
                wr.write(postData);
                wr.flush();
            }
            // 6. 回應資料 ---------------------------------------------------------------------------
            if (conn.getResponseCode() != HttpURLConnection.HTTP_CREATED) {
                int statusCode = conn.getResponseCode();
                System.out.println(statusCode);
            }
        }
    }

# LineNotify-for-Java(上傳檔案圖像版 multipart/form-data)
 * 資源檔：<a href="https://github.com/vincenttuan/LineNotify-for-Java/blob/main/LineNotify/src/main/java/com/HttpPostMultipart.java">HttpPostMultipart.java</a>

    import java.io.File;
    import java.util.Date;
    import java.util.HashMap;
    import java.util.Map;

    public class LineNotifyImageFileDemo {

        public static void main(String[] args) throws Exception {
            // 1. 要發送的資料
            String message = "Hello Java 中文" + new Date();
            // 2. 存取權杖(也稱為:授權 Token)
            String token = "存取權杖";
            // 3. Line Notify 的發送位置
            String lineNotifyUrl = "https://notify-api.line.me/api/notify";
            // 4. 上傳檔案
            File file = new File("src/main/java/com/F18.jpg");
            // 5. 發送前設定 -------------------------------------------------------------------------
            // 標頭檔
            Map<String, String> headers = new HashMap<>();
            headers.put("Authorization", "Bearer " + token);
            HttpPostMultipart multipart = new HttpPostMultipart(lineNotifyUrl, "utf-8", headers);
            // post參數
            multipart.addFormField("message", message);
            // 上傳文件
            multipart.addFilePart("imageFile", file);
            // 返回信息
            String response = multipart.finish();
            System.out.println(response);
        } 

    }

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
        # 不用加入 "Content-Type" : "application/x-www-form-urlencoded"
        headers = {
            "Authorization": "Bearer " + token  
        }

        payload = {'message': msg }
        files = {'imageFile': open(picURI, 'rb')}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload, files = files)
        return r.status_code

    def lineNotifyMessageAndStickerThumbnail(token, msg, picURI, stickerPackageId, stickerId):
        headers = {
            "Authorization": "Bearer " + token
        }

        payload = {
            'message': msg,
            'stickerPackageId': stickerPackageId,
            'stickerId': stickerId,
            'imageThumbnail': picURI,
            'imageFullsize': picURI
        }
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code
    
    
    if __name__ == "__main__":
        token = '存取權杖'
        message = 'Girl 女孩'
        code = lineNotifyMessage(token, message)
        
        #picURI = "img_1.png"  #圖片位置
        #code = lineNotifyMessageAndImage(token, message, picURI)
      
        #picURI = "https://image.cache.u-car.com.tw/articleimage_1091049.jpg"  # 圖片網路位置
        #code = lineNotifyMessageAndStickerThumbnail(token, message, picURI, 1, 113)

        print(code)  
  
# LineNotify-for-Arduino D1mini  Part1
額外開發版網址: https://arduino.esp8266.com/stable/package_esp8266com_index.json <br />
開發版選擇: LOLIN(WEMOS)D1 mini(clone) <br />

    #include <ESP8266WiFi.h>
    #include <WiFiClientSecure.h>

    WiFiClientSecure Secure_client;

    void setup() {
      Serial.begin(9600);
      WiFi.begin("vincenttuan2", "0920947523");
      while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
      }
      Serial.println(WiFi.localIP());
    }

    void loop() {
      if (Secure_client.connect("notify-api.line.me", 443)) {
        Serial.println("send");
        String data = "message=" + String("水位超過警示");
        Secure_client.println("POST /api/notify HTTP/1.1");
        Secure_client.println("Host: notify-api.line.me");
        Secure_client.println("Authorization: Bearer Nj5aoSCYDjH3FB8jBKBSpdnioUjy7koS2zDHGUFUYFR");
        Secure_client.println("Content-Type: application/x-www-form-urlencoded");
        Secure_client.print("Content-Length: ");
        Secure_client.println(data.length());
        Secure_client.println();
        Secure_client.println(data);
        Secure_client.stop();
        Serial.println("stop");
      } else {
        Serial.println("error");
      }
      delay(5000);
    }

# LineNotify-for-Arduino D1mini  Part2
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
  
其他語言支援:
http://white5168.blogspot.com/2017/01/line-notify-4-line-notify.html#.YnoI0RNBzok
