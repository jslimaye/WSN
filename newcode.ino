#include<SPI.h>
#include<RF24.h>
#include<string.h>

// ce, csn pins
RF24 radio(9,10);

//int sensorValue;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600); 
    radio.begin();
    radio.setPALevel(RF24_PA_MAX);
    radio.setChannel(0x70);
    radio.openWritingPipe(0xE8E8F0F0E1LL);
    radio.enableDynamicPayloads();
    radio.powerUp(); 
}

void loop() {
  // put your main code here, to run repeatedly:
String sensorValue = (String)analogRead(A0);       // read analog input pin 0
//Serial.print("AirQuality=");
//Serial.print(sensorValue);               // prints the value read
//Serial.println(" PPM");
//strcat(sensorValue ,"#");

//Serial.print("The value of the temperature sensor is: ");
//Serial.print(celsius);
//Serial.println(" degrees Celsius, ");
char text[100];
int i = 0;
char c = sensorValue[i];
while (c != '\0') {
  text[i] = c;
  i++;
  c = sensorValue[i];
}
strcat(text,"#");

int rawvoltage= analogRead(A1);
float millivolts= (rawvoltage/1024.0) * 500;
String celsius= (String)(millivolts/10);

Serial.println(celsius);

int k = strlen(text);
int j = 0;
char d = celsius[j];
while (d != '\0') {
  text[k] = d;
  j++;
  k++;
  d = celsius[j];
}

Serial.println(text);
//Serial.println(celsius);
radio.write(&text, sizeof(text));
delay(3000);


}
