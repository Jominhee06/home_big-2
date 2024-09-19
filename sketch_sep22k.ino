#include <SoftwareSerial.h>

int tx = 12;
int rx = 13;

SoftwareSerial pad_serial(tx,rx);

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    pad_serial.begin(9600);
    pinMode(8,OUTPUT);

}
  // char ch;
  // String str;

void loop() {
  // put your main code here, to run repeatedly:
    
    char LED;

    if(pad_serial.available())
      Serial.write(pad_serial.read());
    if(Serial.available())
      pad_serial.write(Serial.read());
    
    // if(Serial.available()){

    //     char input = Serial.read();

    //     Serial.println(input);
    // }
    // if(Serial.available() == 0)
    // {
    // Serial.println(str);
    //   str = "";
    // }
    // if(Serial.available()>0)
    // {
    if(pad_Serial.available())
    {  
      LED = pad_serial.read();
      Serial.println(LED);
    //   Serial.write(LED);
    //   Serial.write("n");
    if(LED == 'o')
    {
      digitalWrite(8,HIGH);
    }
    else if(LED == 'x')
    {
      digitalWrite(8,LOW);
    }
  }

  if(Serial.available()){
      char input = Serial.read();
      pad_Serial.Write(input);
  }
  //Serial.print(LED)Serial.read()
  delay(100);
}