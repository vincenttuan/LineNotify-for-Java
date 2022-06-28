package com.linenotify;
/*
 * https://notify-bot.line.me/zh_TW/
 * 右上方-登入
 * 右上方-選擇「個人頁面」
 * 發行存取權杖（開發人員用）
 * 選定傳送對象與群組
 * */
public class Application {
	private static final String USER_TOKEN = "發行存取權杖";

	public static void main(String[] args) {
		System.out.println("Hello World!");

		LineNotify ln = new LineNotify(USER_TOKEN);
		try {
			ln.notifyMe("Line Notify 測試 for Java");
		} catch (Exception ex) {
			System.err.println(ex);
		}
	}
}
