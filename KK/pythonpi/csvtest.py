
# -*- coding: utf-8 -*-
import csv
f = open('example.csv', 'r')
for row in csv.DictReader(f, ["A日期", "B成交股數", "C成交金額", "D成交筆數", "E指數", "F漲跌點數"]):
    print row['E指數']

    Serial.println("濕度Humidity (%);攝氏Temperature (oC);華氏Temperature (oF);克氏溫標Temperature (K);露点温度Dew Point (oC);露点温度Dew Point Slow (oC);麥克風數字值 Mic Digital Value; 煙霧類比Smoke A Value;煙霧數位Smoke D Value;");