#define RED 11
#define GREEN 10
#define BLUE 9


void setup() {
  // put your setup code here, to run once:
    //attachInterrupt(0,LED,RISING);
    pinMode(RED,OUTPUT);
    pinMode(GREEN,OUTPUT);
    pinMode(BLUE,OUTPUT);
    pinMode(6,OUTPUT);
    pinMode(7,INPUT);
    Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
      static int LED;
      
      unsigned int dis = 0;  // unsigned를 쓰면 값이 안튄다.,부호없는 정수)는 2바이트 값을 저장하는 int와 똑같다. 그러나 음수를 저장하는 대신 양수(0 에서 65,535((2^16) - 1)의 범위) 만 저장한다.
      
      digitalWrite(6,HIGH);
      delayMicroseconds(10); // Microseconds = 아두이노 보드에서 스케치 프로그램을 시작하여 흐른 시간을 us(마이크로세컨드: microsecond) 단위의 숫자로 돌려 주는 기능
      digitalWrite(6,LOW);
      dis = pulseIn(7,HIGH);  // pulseIn = 아두이노 핀으로 입력되는 펄스의 시간을 측정하는 함수
      dis = dis * 17 / 1000; // cm 변환
      Serial.println(dis);
      delay(5);

      if(dis < 10 )
      {
        digitalWrite(RED,HIGH);
        digitalWrite(GREEN,LOW);
        digitalWrite(BLUE,LOW);
      }
      else if(dis < 20)
      {
        digitalWrite(RED,LOW);
        digitalWrite(GREEN,HIGH);
        digitalWrite(BLUE,LOW);
      }
      else
      {
        digitalWrite(RED,LOW);
        digitalWrite(GREEN,LOW);
        digitalWrite(BLUE,HIGH);
      }

}