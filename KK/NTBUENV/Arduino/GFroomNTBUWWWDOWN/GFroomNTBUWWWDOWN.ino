// 動手做16-5：從瀏覽器控制遠端的燈光開關
// 詳細的程式說明，請參閱書本16-31頁，
// 以及筆者的網站：sddivid.tw
/////////////////腳位未整理
#include "SPI.h"
#include "Ethernet.h"
#include "WebServer.h"
#include <idDHT11.h>
#include "Streaming.h"

//////////////
int sensorValue = 1;  //輸出煙霧類比訊號用的PIN######
int Led = 13;                                          //設定LED腳位為第13孔
int buttonpin = 4;                                  //設定感測器D0腳位為第3孔
int Key1Pin = 6;  //輸出煙霧數位訊號用的PIN
int val;                                                     //設定變量val

int idDHT11pin = 2; //Digital pin for comunications
int idDHT11intNumber = 0; //interrupt number (must be the one that use the previus defined pin (see table above)
void dht11_wrapper(); // must be declared before the lib initialization

idDHT11 DHT11(idDHT11pin, idDHT11intNumber, dht11_wrapper);
/////////////

const byte NUM_OF_SW = 6;
const byte NUM_OF_DATA = 1;  ////////資料迴圈之行次數
const byte swPins[] = {3, 5, 6, 7, 8, 9};
const char *swNames[] = {"大門", "照明燈", "機櫃門1", "機櫃門2", "機櫃門3", "機櫃門4"};
boolean ledState = LOW;        // LED狀態
unsigned long startTime;       // 儲存起始時間
static byte mac[] = { 0xF0, 0x7B, 0xCB, 0x4B, 0x7C, 0x9F };
IPAddress ip(192, 168, 50, 107);
IPAddress subnet(255, 255, 255, 0);
IPAddress gateway(192, 168, 1, 1);

WebServer webserver("", 80);
////////////////////////
EthernetServer server(80);
//////////////////////

P(htmlHead) = "<!doctype html><html>"
              "<head><meta charset='utf-8'>"
              "<meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0'>"
              "<title>arduino@home</title>";

P(myCSS) = "<style type='text/css'>body {font-family:'微軟正黑體','黑體-繁',sans-serif;background-color:#CCC;}\n"
           ".sw {margin:0 0.5em;font-weight:bolder;}\n"
           ".on {color:#F00;}\n"
           ".off {color:#090;}\n"
           "#lights {border-radius:10px;-moz-border-radius:10px;-webkit-border-radius:10px;background-color:#FFFFFF;padding:1px;}\n"
           "#lights ul {list-style-type:none;padding-left:0px;font-size:24pt;}\n"
           "#lights ul li {margin:10px 0;border-bottom:1px dotted #CCCCCC;padding-bottom:5px;}\n"
           "#lights ul li a {display:block;text-decoration:none;color:#000;}\n</style>";

P(htmlFoot) = "</body></html>";

// 顯示網頁內容
void showPage(WebServer &server) {
  server.printP(htmlHead);
  server.printP(myCSS);
  server.println("</head><body><h1 align='center'>各式開關</h1><div id='lights'><ul>");


  for (byte i = 0; i < NUM_OF_SW; i++) {////////各式開關
    server << "<li><a href='sw?id=" << i << "'>";
    // 依照開關腳位的狀態顯示ON或OFF
    if (digitalRead(swPins[i]) == 1) {
      server.println("<span class='sw on'>ON</span>");
    } else {
      server.println("<span class='sw off'>OFF</span>");
    }
    server << swNames[i] << "</a></li>";
  }
  
  /////////////////加入數值/////////////////////////
  int keystate = digitalRead(Key1Pin); // 取得煙霧輸入PIN 腳的值
  val = digitalRead(buttonpin);
  if (val == HIGH)                                    //當感測器测有信號時，LED閃爍
  {
    digitalWrite(Led, HIGH);
  }
  else
  {
    digitalWrite(Led, LOW);
  }
  server.println("<body><li><h1 align='center'>各式數值</h1><div id='lights'><H2 align='center'>");
  server.print("<span class='sw off'>濕度      Humidity (oC): </span>");
  server.print(DHT11.getHumidity(), 2);
    server.print("<HR color='#696969' size='10' >");
  server.print("<span class='sw off'>攝氏      Temperature (oC): </span>");
  server.print(DHT11.getCelsius(), 2);
   server.print("<HR color='#696969' size='10' >");
  server.print("<span class='sw off'>華氏      Temperature (oF): </span>");
  server.print(DHT11.getFahrenheit(), 2);
   server.print("<HR color='#696969' size='10' >");
    delay(1000);


  server.println("</H2></li></ul></div>");
  server.printP(htmlFoot);
}

void defaultCmd(WebServer &server, WebServer::ConnectionType type, char *, bool)
{
  server.httpSuccess();

  if (type != WebServer::HEAD)
  {
    // 顯示網頁內容
    showPage(server);
  }
}

void getCmd(WebServer &server, WebServer::ConnectionType type, char *url_tail, bool tail_complete)
{
  URLPARAM_RESULT rc;
  char name[3], value[3];
  byte rawNum, pinNum;
  server.httpSuccess();

  if (type == WebServer::GET) {
    // 讀取參數
    while (strlen(url_tail)) {
      rc = server.nextURLparam(&url_tail, name, 3, value, 3);
      if (strcmp(name, "id") == 0) {
        rawNum = atoi(value);
        pinNum = swPins[rawNum];
        Serial.print("id num: ");
        Serial.println(rawNum);
        Serial.print("pin num: ");
        Serial.println(pinNum);
        digitalWrite(pinNum, !digitalRead(pinNum));
      }
    }

    // 顯示頁面
    showPage(server);
  }
}

void setup() {
  int result = DHT11.acquireAndWait();
  Serial.begin(9600);
  // 設定輸出腳位
  for (byte i = 0; i < NUM_OF_SW; i++) {
    pinMode(swPins[i], OUTPUT);
  }
  pinMode(Led, OUTPUT);                    //設定LED为输出
  pinMode(buttonpin, INPUT);             //設定感測器D0为輸入

  Serial.println("idDHT11 Example program");

  Serial.print("LIB version: ");

  Serial.println(IDDHT11LIB_VERSION);

  Serial.println("---------------");

  Ethernet.begin(mac, ip, gateway, subnet);
  webserver.setDefaultCommand(&defaultCmd);     // 處理「首頁」請求
  webserver.addCommand("sw", &getCmd);         // 處理「sw頁面」請求
  webserver.begin();
}

void dht11_wrapper() {

  DHT11.isrCallback();

}
void loop() {
  webserver.processConnection();

 

}
