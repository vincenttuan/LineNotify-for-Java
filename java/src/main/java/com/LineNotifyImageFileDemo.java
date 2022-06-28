package com;

import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

import javax.xml.transform.Source;

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
