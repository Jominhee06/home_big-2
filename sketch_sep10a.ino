//풀업 저항

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(8, OUTPUT);
  pinMode(6, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int readValue = digitalRead(6);  // 입력핀의 값을 읽어 변수에 저장
  Serial.println(readValue);       // 변수의 값을 시리얼 모니터에 출력

  if (readValue == LOW) {  // 입력 값에 따라 LED 출력값 제어
    digitalWrite(8, HIGH);
  } else {
    digitalWrite(8, LOW);
  }
}
