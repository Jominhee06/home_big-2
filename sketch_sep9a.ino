//static int state = 0;
void eos()
{
  //static bool state = HIGH;
  static int state = 0;
  //digitalWrite(13, state);
  //state = !state;
    //state -= 1000;
    //static int state = 0;
    //Serial.println(state);
    //state++;
  Serial.println(state++);
}

void setup() {
  // put your setup code here, to run once:
  //attachInterrupt(0, eos, FALLING);
    attachInterrupt(0, eos, RISING); //  두 가지 종류의 인터럽트(타이머 인터럽트,하드웨어 인터럽트)중 하드웨어 인터럽트를 사용할 수 있게 해주는 함수
    Serial.begin(9600);
    pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    //Serial.println(digitalRead(2));
    //Serial.println(state++);
}
