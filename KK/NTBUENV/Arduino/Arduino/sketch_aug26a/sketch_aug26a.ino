
int sensorValue = 0;  //輸出類比訊號用的PIN
int Key1Pin = 4;  //輸出數位訊號用的PIN
//int ledPin1 = 13; //設定警告用LED
void setup()
{
  Serial.begin(9600); // 設定Serial 傳輸速度
  //pinMode(Key1Pin, OUTPUT); // 這裡設定所要發出警告的PIN腳模式
}
void loop()
{
  Serial.print("Value: ");
  sensorValue = analogRead(0); //讀取數位 pin 0
  Serial.print(sensorValue, DEC); // 顯示類比資料
  delay(100); //休息0.1秒
  int keystate = digitalRead(Key1Pin); // 取得輸入PIN 腳的值
  Serial.print("  Digital Value: ");
  Serial.print(keystate, DEC); // 顯示數位資料
//  if (keystate == 0)
//  {
//    Serial.print(" Safe"); // 安全
////    digitalWrite(ledPin1, LOW); // 正常
//  } else {
//    Serial.print(" Help"); // 偵測到了
////    digitalWrite(ledPin1, HIGH); // 發出警告
//  }
  Serial.println(" ");
}
