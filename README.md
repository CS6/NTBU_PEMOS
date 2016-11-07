# NTBU_PEMOS
<<<<<<< HEAD
=======
# NTBU_PEMOS
>>>>>>> a85eaa6d6caac089d7d5755fd58082bba9ea50ba
 
 
 
#完整教學
https://www.gitbook.com/book/cs6/ntbu/details
 
!!Python 的 mySQLdb已停止支援，建議跟換或使用替代的套件!! 
 

ArduinoX Raspberry Pi
之
土炮環境監控
 
 
 
 
 
 
 
 
 
 
 
 
 
 
作者：林大元。市立大安高級工業職業學校。綜高三愛

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

研究動機
在這個網路發達的年代，物聯網是一項重要的發展，然而為了連上網路勢必需要機房的運作，
為了讓我們可以隨時知道機房的狀況促使我進行這項研究。


研究目的
使用Arduino連接感測器，並傳送數值給樹梅派，經過樹梅派處裡數值後再透過在設於樹梅派上的server發送服務




(1)系統架構


Arduino負責結合各式感測器的數值，製作成資料格式後，透過USB將數值串送給RPI，
RPI則透過Python，取得數據後轉存成CSV格式紀錄，並且將取得之資料上傳至MYSQL的資料表中，
再透過PHPmyADMIN於RPI上架設網頁伺服器，並以網頁讀取SQL資料呈現給使用者檢視，
並且在網頁輸入指令後，透過RPI回傳給Arduino控制開關。
同一時間RPI將取得之數值透過MQTT伺服器發布給訂閱裝置，
使用者即可隨時隨地的獲取最新的狀況。




 
(圖一)
 
 


 (2)使用零件

(圖二)

表格：




(表一)使用零件


| 開發版  | Arduino  | Raspberry Pi |
| :------------ |:---------------:| -----:|
|    光敏感測器  |  機櫃上方        | 是否開燈 |
|    MQ2感測器  | 機櫃上方         | 偵測MQ2 |
|     MQ5感測器  | 機櫃上方  | 偵測MQ5 |
| 火焰感測器  | 機櫃內側後方  | 偵測有無火源 |
| 紅外線感測器  | 機櫃上方  | 偵測有無人員 |
| 微動開關  | 機櫃內側與門之夾縫  | 是否開門 |
| 蜂鳴器  | 機櫃內側  | 警示，提示異常 |
| 敲擊感測器  | 機櫃下方地板  | 偵測人員行經 |
| 加速度感測器  | 機櫃上方  | 機櫃偏移狀況 |
| LED  | 滅火器旁  | 警示，提示使用滅火氣 |
| 麥克風  | 機櫃上方  | 偵測有無人聲 |
| 溫溼度感測器  | 機櫃上方  | 偵測溫溼度 |
| 網路攝影機  | 機櫃上方  | 監視器 |
| 不斷電系統  | 機櫃內側後方  | 確保電力共應 |
| 網路線  | 開發版之間  | 連接開發版 |












































 (3)Sensor端設計

(圖三)

(圖四)                                                  (圖五)


機櫃上方為[加速度、紅外線，溫溼度，MQ5&3]放置區域，透過感測器可獲得[有無人員經過，溫溼度，氣體比例，機櫃是否移動，煙霧]的狀態。


機櫃下方為[敲擊，震動，紅外線]放置區域，透過感測器可獲得[有無人員經過]的狀態。





於滅火器旁放置LED，根據火焰感測器的數值判斷是否需要使用滅火器
 (4)server端設計
 
(圖六)








表(二)
軟體
用途
MQTT
推送訊息
MySQL
資料庫管理
phpMyAdmin
架設伺服器
Python
程式語言
RASPBIAN
Raspberry Pi 作業系統



















(圖七)

 
  (圖八)
 
表(三)
軟體
用途
WMQTT Utility
測試&調整MQTT
mobaXterm
SSH連線
Arduino
纂寫Arduino程式
Sublime Text
纂寫Raspberry Pi 程式
三.結論


	成果
 
(圖九)


使用者管理介面，可直接透過此介面進行管理，亦是觀測介面，一目瞭然的排版方式讓用戶一眼了解機房現狀。



(圖十)


實際零件裝配圖(為了方便識別並無按照真實電路配線)


 






 


