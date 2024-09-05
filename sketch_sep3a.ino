// 변수 지정을해서 설정해도 된다. 설정값만 바꿈
void setup() {
  // put your setup code here, to run once:
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(13, OUTPUT);
}
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(13, HIGH);
  delay(2000);
  
  digitalWrite(10, HIGH); 
  digitalWrite(11, LOW);
  digitalWrite(13, HIGH);
  delay(2000);
  
  digitalWrite(10, LOW); 
  digitalWrite(11, HIGH);
  digitalWrite(13, LOW);
  delay(2000);
}
