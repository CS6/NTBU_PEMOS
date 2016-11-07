#include <Wire.h>  
 #define SLAVE_ADDRESS 0x40   // Define the i2c address

#include <dht.h>

dht DHT;

#define DHT11_PIN 4

char tempera[5];
 void setup()
 {
 Serial.begin(9600);
 Wire.begin(SLAVE_ADDRESS); 

}

void loop()
 {
 // READ DATA
 Serial.print(“DHT11, \t”);
int chk = DHT.read11(DHT11_PIN);
 switch (chk)

{
 case DHTLIB_OK:
 Serial.print(“OK,\t”);
break;
 case DHTLIB_ERROR_CHECKSUM:
 Serial.print(“Checksum error,\t”);
break;
 case DHTLIB_ERROR_TIMEOUT:
 Serial.print(“Time out error,\t”);
break;
 case DHTLIB_ERROR_CONNECT:
 Serial.print(“Connect error,\t”);
break;
 case DHTLIB_ERROR_ACK_L:
 Serial.print(“Ack Low error,\t”);
break;
 case DHTLIB_ERROR_ACK_H:
 Serial.print(“Ack High error,\t”);
break;
 default:
 Serial.print(“Unknown error,\t”);
break;
 }
 dtostrf(DHT.temperature, 4, 2, tempera);

Wire.onRequest(sendData); 
 delay(2000);

}

void sendData()

{
 Wire.write(tempera); 

}
