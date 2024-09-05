void setup() {
  // put your setup code here, to run once:
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int i;

  if(Serial.available()) // available -> 수신버퍼에 있는지 없는지를 확인한다. 
  {
    char rx = Serial.read();
    Serial.println(rx);
    if(rx == '1')  // 점점 밝게 하고 멈춤
    {
      for(i = 0; i < 256; i++)
      {
        analogWrite(10, i);
        delay(10);
      }
    }
    else if (rx == '2')  // 점점 흐리게 하고 멈춤
    {
      for(i = 255; i > 0;  i--)
      {
        analogWrite(10, i);
        delay(10);
      }
    }
    analogWrite(10, 0);
  }
}
