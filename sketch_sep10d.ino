// 가변저항 이용

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode(10, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    int abc = analogRead(A0);
    Serial.println(abc);
    Serial.print("\t");
    //abc = map(abc,400,900,0,200);
    Serial.println(abc);
    
    if(abc > 0){
      digitalWrite(10,HIGH);
    }
}
