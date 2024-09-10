int pre_time = 0;
int cur_time = 0;

void btn()
{
  static int cnt = 0;
  cur_time = millis(); // 밀리단위로 초 단위 계산
  if(cur_time - pre_time >= 500)
  {
    Serial.println(++cnt);
    pre_time = cur_time;
  }
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  attachInterrupt(0, btn, RISING);
  //pinMode(2,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println(millis());
}
