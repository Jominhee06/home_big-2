#define RED  8
#define GREEN  7
#define BLUE  6
int cur_time = 0;
int pre_time = 0;

void setup() {
  // put your setup code here, to run once:
  attachInterrupt(0,RGB,RISING);
  pinMode(RED,OUTPUT);
  pinMode(GREEN,OUTPUT);
  pinMode(BLUE,OUTPUT);
  Serial.begin(9600);   
}

void loop() {
  // put your main code here, to run repeatedly:
  
}

void RGB()
{   
    static int rgb = 0;
    static int cnt = 0;
    cur_time = millis(); // 
    if(cur_time - pre_time >= 500) //  
    {
      Serial.println(cnt);
      pre_time = cur_time;  
    rgb++;
    if(rgb > 3) rgb = 1; 
    }
   switch(rgb){ 
    case 1:
      digitalWrite(RED,HIGH);
      digitalWrite(GREEN,LOW);
      digitalWrite(BLUE,LOW);
      break;

    case 2:
      digitalWrite(RED,LOW);
      digitalWrite(GREEN,HIGH);
      digitalWrite(BLUE,LOW);
      break;

     case 3:
       digitalWrite(RED,LOW);
       digitalWrite(GREEN,LOW);
       digitalWrite(BLUE,HIGH);
       break;
   }
}
