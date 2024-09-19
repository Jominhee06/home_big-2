#define pas 11
#include <Servo.h>
#include <Keypad.h>

Servo servo;


const byte ROWS = 4;
const byte COLS = 4;

char * Code = "1234";
int position = 0;
int wrong = 0;

char keys[ROWS][COLS] = 
{{'1','2','3','A'},
 {'4','5','6','B'},
 {'7','8','9','C'},
 {'*','0','#','D'}
 };
byte rowPins[ROWS] = {6,7,8,9}; //R1,R2,R3,R4
byte colPins[COLS] = {5,4,3,2}; //C1,C2,C3,C4

Keypad keypad = Keypad(makeKeymap(keys), rowPins,colPins,ROWS,COLS);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(10);
  pinMode(11,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  char key = keypad.getKey();
  if((key >= '0' && key <= '9') || (key>='A' && key<='D')||(key == '*'||key=='#'))
  {
    Serial.println(key);
    tone(pas, 523, 500);
    if(key == '*' || key == '#'){
      position = 0;
      wrong = 0;
      setLocked(true);

    }
    else if(key == Code[position])
    {
      position++;
      wrong = 0;
    }  
    
    else if(key!=Code[position])
    {
      position = 0;
      setLocked(true);
      wrong++;
    }
    if(position == 4)
    {
      setLocked(false);
      Serial.println("FULL INPUT");
      position = 0;

    }
    if(wrong == 4)
    {
      Serial.print("Out");
      wrong = 0;
    }
   
  }
   delay(100);
}

void setLocked(int locked)
{
  if(locked)
  {
    Serial.println("Lock");
    //tone(pas, 523, 500);
  }
  else
  {
    Serial.println("UnLock");
    servo.write(180);
    delay(500);
    servo.write(0);
    delay(500);
     tone(pas, 262, 500);
    delay(500);
     tone(pas, 294, 500);
    delay(500);
     tone(pas, 330, 500);
    delay(500);
     tone(pas, 349, 500);
    delay(500);
     tone(pas, 392, 500);
    delay(500);
     tone(pas, 440, 500);
     delay(500);
        tone(pas, 494, 500);
       delay(500);
        tone(pas, 523, 500);
       delay(500);
   
  }
}