// 動手做16-5：從瀏覽器控制遠端的燈光開關
// 詳細的程式說明，請參閱書本16-31頁，
// 以及筆者的網站：sddivid.tw

#include "SPI.h"
#include "Ethernet.h"
#include "WebServer.h"

#include "Streaming.h"

const byte NUM_OF_SW = 6;
const byte swPins[] = {3, 5, 6, 7, 8, 9};
const char *swNames[] = {"大門", "照明燈", "機櫃門1", "機櫃門2", "機櫃門3", "機櫃門4"};

boolean ledState = LOW;        // LED狀態
unsigned long startTime;       // 儲存起始時間
static byte mac[] = { 0xF0, 0x7B, 0xCB, 0x4B, 0x7C, 0x9F };
IPAddress ip(192, 168, 50, 107);
IPAddress subnet(255, 255, 255, 0);
IPAddress gateway(192, 168, 1, 1);

WebServer webserver("", 80);

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
    server.println("</head><body><h1>各式開關</h1><div id='lights'><ul>");
    for (byte i =0; i< NUM_OF_SW; i++) {
      server << "<li><a href='sw?id=" << i << "'>";
      // 依照開關腳位的狀態顯示ON或OFF
      if (digitalRead(swPins[i]) == 1) {
        server.print("<span class='sw on'>ON</span>");
      } else {
        server.print("<span class='sw off'>OFF</span>");
      }
      server << swNames[i] << "</a></li>";
    }
    server.println("</ul></div>");
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
      if (strcmp(name,"id") == 0) {
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
  Serial.begin(9600);
  // 設定輸出腳位
  for (byte i = 0; i < NUM_OF_SW; i++) {
    pinMode(swPins[i], OUTPUT);
  }
  
  Ethernet.begin(mac, ip, gateway, subnet);
  webserver.setDefaultCommand(&defaultCmd);     // 處理「首頁」請求
  webserver.addCommand("sw", &getCmd);         // 處理「sw頁面」請求
  webserver.begin();
}

void loop() {
  webserver.processConnection();
}
