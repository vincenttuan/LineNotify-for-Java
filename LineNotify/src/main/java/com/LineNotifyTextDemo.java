package com;

import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Date;
import java.util.UUID;

import javax.xml.transform.Source;

public class LineNotifyTextDemo {

    public static void main(String[] args) throws Exception {
        // 1. 要發送的資料
        String message = "Hello Java 中文" + new Date();
        // 2. 存取權杖(也稱為:授權 Token)
        String token = "存取權杖";
        // 3. Line Notify 的發送位置
        String lineNotifyUrl = "https://notify-api.line.me/api/notify";
        // 4. 發送前設定 -------------------------------------------------------------------------
        //byte[] postData = ("message=" + message  + "&stickerPackageId=1&stickerId=113").getBytes("UTF-8");
        
        String picurl = "https://image.cache.u-car.com.tw/articleimage_1091049.jpg";
        byte[] postData = ("message=" + message + "&stickerPackageId=1&stickerId=113&imageThumbnail=" + picurl + "&imageFullsize=" + picurl).getBytes("UTF-8");
        
        //int postDataLength = postData.length;
        URL url = new URL(lineNotifyUrl);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setDoOutput(true);
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Authorization", "Bearer " + token); // 一定要加
        //conn.setRequestProperty("Content-Type", "multipart/form-data; boundary=" + UUID.randomUUID().toString());
        
        //conn.setRequestProperty("charset", "utf-8"); // 可以不用加
        //conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded"); // 可以不用加
        //conn.setRequestProperty("Content-Length", Integer.toString(postDataLength)); // 可以不用加
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
    
    public static byte[] mergeBytes(byte[] data1, byte[] data2) {
        byte[] result = new byte[data1.length + data2.length];
        System.arraycopy(data1, 0, result, 0, data1.length);
        System.arraycopy(data2, 0, result, data1.length, data2.length);
        return result;
    } 
    
}
