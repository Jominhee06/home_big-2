#include <Servo.h>

Servo motor;

void setup() {
  // put your setup code here, to run once:
  motor.attach(11);  
}

void loop() {
  // put your main code here, to run repeatedly:
   static int angle = 0;
   motor.write(angle++);
   if(angle > 180)
    angle = 0;
   delay(100);   
}
