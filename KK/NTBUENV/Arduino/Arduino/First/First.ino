int sensorValue = 0;  //輸出煙霧類比訊號用的PIN=D0
int Led = 13;                                          //設定LED腳位為第13孔
int buttonpin = 3;                                  //設定感測器D0腳位為第3孔
int Key1Pin = 4;  //輸出煙霧數位訊號用的PIN
int val;                                                     //設定變量val
void setup()
{
  Serial.begin(9600); // 設定Serial 傳輸速度
  pinMode(Led, OUTPUT);                    //設定LED为输出
  pinMode(buttonpin, INPUT);             //設定感測器D0为輸入
}
void loop()
{
  sensorValue = analogRead(0); //讀取數位 pin 0
 
  val = digitalRead(buttonpin);            //將感測器的值讀取給给val
  Serial.print("Mic Digital Value: ");
  Serial.println(val, DEC); // 顯示數位資料
  int keystate = digitalRead(Key1Pin); // 取得煙霧輸入PIN 腳的值
  Serial.print("Smoke A Value: "); // 顯示煙霧類比資料
  Serial.println(sensorValue, DEC); // 顯示煙霧類比資料
  Serial.print("Smoke D Value: "); // 顯示煙霧數位資料
  Serial.println(keystate, DEC); // 顯示煙霧數位資料
  
  if (val == HIGH)                                    //當感測器测有信號時，LED閃爍
  {
    digitalWrite(Led, HIGH);
  }
  else
  {
    digitalWrite(Led, LOW);
    
  }
  Serial.println(" ");
  delay(100); //休息0.1秒
}




